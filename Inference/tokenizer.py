import re
from collections import Counter, OrderedDict
from torchtext.vocab import vocab

BOS_IDX, PAD_IDX, EOS_IDX, UNK_IDX, SEP_IDX = 0, 1, 2, 3, 4


class Tokenizer:
    """
    Class for tokenizing equations and building vocabularies for source and target sequences.
    """

    def __init__(self, eqns, special_symbols):
        """
        Initializes the Tokenizer with equations.
        Args:
            eqns (list): List of equations to tokenize.
        """
        self.eqns = eqns
        self.identifier = r'[a-zA-Z_][a-zA-Z_0-9]*'
        self.number = r'[0-9]+(?:\.[0-9]*)?'
        self.operator = r'\^|[-+*/=<>()]'
        self.space = r'[ \t]+'
        self.special_symbols = special_symbols

    @staticmethod
    def _extract(eqn, ord_dict, pattern):
        """
        Extracts tokens from the equation and updates the dictionary with token counts.
        """
        elems = pattern.findall(eqn)
        elem_counts = Counter(elems)
        for key, value in elem_counts.items():
            if key not in ord_dict:
                ord_dict[key] = value
            else:
                ord_dict[key] += value
        return ord_dict

    @staticmethod
    def _add_separators(match):
        """
        Adds separators around operators in the equation for easier splitting.
        """
        return f";{match.group(0)};"

    @staticmethod
    def _preprocess_eqn(data):
        """
        Preprocesses the equation by replacing '**' with '^' and adding spaces around operators.
        """
        data = re.sub(r'\*\*', '^', data)
        for r in (('{', ' {'), ('}', '}'), (' + ', ' + '), ('*', ' * '), ('-', ' - '), ('+', ' + '),
                  ('^', '^'), ('(', ' ('), (')', ')'), ('/', ' / '), ('  ', ' '), (' - ', ' - '), ('( (', '((')):
            data = data.replace(*r)
        return data.strip()

    def build_tgt_vocab(self):
        """
        Builds vocabulary for target sequences.
        """
        ordered_dict = OrderedDict()
        exps = [self.space, self.identifier, self.number, self.operator]
        for eqn in self.eqns:
            eqn = self.preprocess_eqn(eqn)
            for exp in exps:
                ordered_dict = self._extract(
                    eqn, ordered_dict, re.compile(exp))
        voc = vocab(
            ordered_dict, specials=self.special_symbols[:-1], special_first=True)
        voc.set_default_index(UNK_IDX)
        return voc

    def build_src_vocab(self):
        """
        Builds vocabulary for source sequences.
        """
        ordered_dict = OrderedDict()
        for i in range(10):
            ordered_dict[str(i)] = 1
        ordered_dict['-'] = 1
        ordered_dict['.'] = 1
        voc = vocab(ordered_dict, specials=self.special_symbols,
                    special_first=True)
        voc.set_default_index(UNK_IDX)
        return voc

    def src_tokenize(self, expr):
        """
        Tokenizes source equations.
        """
        pattern = r'\d'
        expr = re.sub(pattern, r';\g<0>;', expr)
        # Replace multiple semicolons with single semicolon
        expr = re.sub(r';{2,}', ';', expr)
        expr = re.sub(r'\s+', '<sep>', expr)
        expr = re.sub('-', ';-;', expr)
        expr = re.sub(r';{2,}', ';', expr)
        toks = expr.split(';')
        toks[0] = '<s>'
        toks[-1] = '</s>'
        return toks

    def tgt_tokenize(self, expr):
        """
        Tokenizes target equations.
        """
        exps = [self.space, self.identifier, self.operator]
        expr = self.preprocess_eqn(expr)
        for exp in exps:
            expr = re.sub(exp, self.add_separators, expr)
        # Replace multiple semicolons with single semicolon
        expr = re.sub(r';{2,}', ';', expr)
        toks = expr.split(';')
        toks[0] = '<s>'
        toks[-1] = '</s>'
        return toks

    def src_decode(self, tokens):
        """
        Decodes source tokens into equation string.
        """
        expr = ' '.join(tokens[1:-1])  # Exclude <s> and </s> tokens
        expr = expr.replace('<sep>', ' ')
        expr = expr.replace(';', '')  # Remove any remaining semicolons
        expr = expr.replace('- ', '-')  # Remove space after minus sign
        return expr

    def tgt_decode(self, tokens):
        """
        Decodes target tokens into equation string.
        """
        expr = ''.join(tokens[1:-1])  # Exclude <s> and </s> tokens
        expr = expr.replace('<sep>', ' ')
        return expr

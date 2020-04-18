class tab:
    def __init__(self, i=0):
        self.i = i

    def __enter__(self):
        tmp = self.i + 1
        return tab(tmp)

    def tab_print(self, inp_str):
        print("    " * self.i + inp_str)

    def __exit__(self, *args):
        pass


with tab() as indent:
    indent.tab_print('привет!')
    with indent as ind:
        ind.tab_print('здорово')
        with ind as i:
            i.tab_print('бонжур')
    indent.tab_print('эй')

# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class ContainerMain(BoxLayout):
    def update_label(self):
        self.lbl.text = self.formula

    def add_number(self, instance):
        try:
            if self.res == 10:
                self.res = 0
                self.formula = ""
            if self.formula == "0":
                self.formula = ""

            self.formula += str(instance)
            for i in self.formula:
                if i in "()":
                    if self.num != "":
                        self.fin += f"{float(self.num):,}".replace(",", " ")
                        self.num = ""
                    self.fin += i
                if self.formula[0] == "-" and self.minus == 0:
                    self.minus = 10
                    self.num += "777"
                if i in "1234567890.":
                    self.num += i
                if i in "-+*/%":
                    if self.formula[0] == "-" and self.minus == 10:
                        self.minus = 20
                    if self.num != "":
                        self.fin += f"{float(self.num):,}".replace(",", " ")
                        self.num = ""
                    self.fin += i

            if self.num != "":
                self.formula = self.fin + f"{float(self.num):,}".replace(",", " ")
                self.num = ""
            self.fin = ""
            self.formula = self.formula.replace(".0", "")
            if self.minus == 20:
                self.formula = self.formula[3:]
                self.minus = 0
            elif self.minus == 10:
                self.minus = 0
            self.update_label()
        except:
            self.minus = 0
            self.lbl.text = '0'
            self.formula = "0"
            self.fin = ""

    def add_operation(self, instance):
        check = str(instance).lower()

        if self.res == 10:
            self.res = 0
            pass
        if self.formula == "0":
            self.formula = ""
            if check == "(":
                self.formula += str(instance)
                self.update_label()
                return
            if (str(instance).lower() == "."):
                self.formula += "0"
            else:
                if (check == "-"):
                    self.formula += str(instance)
                    self.update_label()
                    return
                if (check == "+") or (check == "*") or (check == "/"):
                    self.lbl.text = '0'
                    self.formula = "0"
                    return self.formula
        # if (check == "×"):
        #     self.formula += "*"
        if (self.formula[-1] == "+") or (self.formula[-1] == "*") or (self.formula[-1] == "/") \
                or (self.formula[-1] == "-") or (self.formula[-1] == "%"):
            if (self.formula[0] == "-"):
                return
            self.formula = self.formula[:-1]
            self.formula += str(instance)

            self.update_label()
            return
        else:
            self.formula += str(instance)

        self.update_label()

    def par_and_per(self, instance):
        try:
            if (str(instance).lower() == "%"):
                self.formula += "*0."
                self.update_label()
                return self.formula
            if self.formula == "0":
                self.formula = ""
                if (str(instance).lower() == "("):
                    self.formula += "("
                    self.update_label()
                    return self.formula
                if (str(instance).lower() == "%"):
                    self.lbl.text = '0'
                    self.formula = "0"
                    return self.formula
                if (str(instance).lower() == ")"):
                    self.formula += "("
            self.formula += str(instance)
            if len(self.formula) > 1:
                if self.formula[-2] in "1234567890" and self.formula[-1] == "(":
                    self.formula = self.formula[:-1] + "*("
            if self.formula == "()":
                self.formula = ""
                self.formula = "("
            elif (str(instance).lower() == ")"):
                if "(" in self.formula:
                    pass
                else:
                    self.formula = self.formula[:-1]
                    self.formula += "("
            self.update_label()
        except:
            self.lbl.text = '0'
            self.formula = "0"

    def calculate(self):
        try:
            self.lbl.text = str(eval(self.lbl.text.replace(" ", "")))
            self.formula = "{0:,.2f}".format(float(self.lbl.text)).replace(",", " ")
            self.formula = self.formula.replace(".00", "")
            self.update_label()
            self.res = 10

        except:
            self.lbl.text = '0'
            self.formula = "0"

    def clear(self):
        self.lbl.text = '0'
        self.formula = "0"

    def backspace(self):
        try:
            if self.res == 10:
                self.res = 0
                self.lbl.text = '0'
                self.formula = "0"
                self.update_label()
                return

            self.formula = self.formula[:-1]
            if self.formula == "":
                self.lbl.text = '0'
                self.formula = "0"
            for i in self.formula:
                if i in "()":
                    if self.num != "":
                        self.fin += f"{float(self.num):,}".replace(",", " ")
                        self.num = ""
                    self.fin += i
                if self.formula[0] == "-" and self.minus == 0:
                    self.minus = 10
                    self.num += "777"
                if i in "1234567890.":
                    self.num += i
                if i in "-+*/%":
                    if self.formula[0] == "-" and self.minus == 10:
                        self.minus = 20
                    if self.num != "":
                        self.fin += f"{float(self.num):,}".replace(",", " ")
                        self.num = ""
                    self.fin += i

            if self.num != "":
                self.formula = self.fin + f"{float(self.num):,}".replace(",", " ")
                self.num = ""
            self.fin = ""
            self.formula = self.formula.replace(".0", "")
            if self.minus == 20:
                self.formula = self.formula[3:]
                self.minus = 0
            elif self.minus == 10:
                self.minus = 0
            self.lbl.text = self.formula
            if self.formula == "":
                self.lbl.text = '0'
                self.formula = "0"
        except:
            self.minus = 0
            self.formula = self.fin.replace(".0", "")
            self.lbl.text = self.formula
            self.fin = ""


class CalculatorMainApp(App):
    def build(self):
        return ContainerMain()


if __name__ == "__main__":
    CalculatorMainApp().run()

import tkinter as tk
from tkinter import ttk
import math

# --- CONFIGURATION ---
XP_BG = "#ECE9D8"
XP_WHITE = "#FFFFFF"
XP_BLUE = "#316AC5"
FONT_MAIN = ("Tahoma", 9)
FONT_DISPLAY = ("Tahoma", 14, "bold")

class RetroScientificCalc:
    def __init__(self, root):
        self.root = root
        self.root.title("Installation Calc Setup")
        self.root.geometry("450x600")
        self.root.minsize(400, 550)
        self.root.configure(bg=XP_BG)

        self.expression = ""
        self.equation = tk.StringVar()
        
        # UI Setup
        self.setup_layout()
        self.create_msi_banner()
        self.create_menu_icon()
        self.main_container = tk.Frame(self.root, bg=XP_BG)
        self.main_container.pack(expand=True, fill="both")
        
        self.create_sidebar()
        self.show_calculator_mode() # Default mode
        self.bind_keys()

    def setup_layout(self):
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)

    def create_msi_banner(self):
        self.banner_frame = tk.Frame(self.root, bg=XP_WHITE, height=70, bd=0)
        self.banner_frame.pack(side="top", fill="x")
        self.banner_frame.pack_propagate(False)
        
        self.lbl_title = tk.Label(self.banner_frame, text="Advanced System Setup", 
                             bg=XP_WHITE, font=("Tahoma", 11, "bold"), anchor="w")
        self.lbl_title.pack(padx=15, pady=(10, 0), fill="x")
        
        self.lbl_desc = tk.Label(self.banner_frame, text="Select a mode from the menu...", 
                            bg=XP_WHITE, font=("Tahoma", 8), anchor="w", fg="#666")
        self.lbl_desc.pack(padx=25, pady=0, fill="x")

    def create_menu_icon(self):
        self.menu_btn = tk.Label(self.banner_frame, text="≡", bg=XP_WHITE, 
                                 font=("Arial", 24), cursor="hand2")
        self.menu_btn.place(relx=0.97, rely=0.2, anchor="ne")
        self.menu_btn.bind("<Button-1>", lambda e: self.toggle_sidebar())

    def create_sidebar(self):
        self.sidebar = tk.Frame(self.root, bg=XP_BLUE, width=0)
        self.sidebar_open = False
        
        tk.Label(self.sidebar, text="SYSTEM MODES", bg=XP_BLUE, fg="white", 
                 font=("Tahoma", 10, "bold")).pack(pady=20)
        
        modes = [
            ("Calculator", self.show_calculator_mode), 
            ("Multi-Converter", self.show_converter_mode),
            ("Programmer Base", self.show_programmer_mode),
            ("Finance Setup", self.show_finance_mode)
        ]
        
        for name, cmd in modes:
            btn = tk.Button(self.sidebar, text=name, font=FONT_MAIN, bg=XP_WHITE, 
                            relief="flat", command=cmd, cursor="hand2")
            btn.pack(fill="x", padx=15, pady=8)

    def toggle_sidebar(self):
        if not self.sidebar_open:
            self.sidebar.place(relx=1.0, rely=0.11, anchor="ne", relheight=0.89, relwidth=0.5)
            self.sidebar.lift()
            self.sidebar_open = True
        else:
            self.sidebar.place_forget()
            self.sidebar_open = False

    def clear_container(self):
        for widget in self.main_container.winfo_children():
            widget.destroy()

    # --- CALCULATOR MODE ---
    def show_calculator_mode(self):
        self.clear_container()
        self.lbl_desc.config(text="Performing scientific computations...")
        if self.sidebar_open: self.toggle_sidebar()

        display_frame = tk.Frame(self.main_container, bg=XP_BG)
        display_frame.pack(pady=15, padx=15, fill="x")
        
        self.input_field = tk.Entry(display_frame, textvariable=self.equation, 
                               font=FONT_DISPLAY, justify='right',
                               bg=XP_WHITE, bd=2, relief="sunken",
                               state="readonly", readonlybackground=XP_WHITE)
        self.input_field.pack(ipady=10, fill="x")

        btns_frame = tk.Frame(self.main_container, bg=XP_BG)
        btns_frame.pack(expand=True, fill="both", padx=10, pady=5)

        for i in range(5): btns_frame.columnconfigure(i, weight=1)
        for i in range(1, 7): btns_frame.rowconfigure(i, weight=1)

        buttons = [
            ('sin', 1, 0), ('cos', 1, 1), ('tan', 1, 2), ('C', 1, 3),  ('DEL', 1, 4),
            ('log', 2, 0), ('ln', 2, 1),  ('(', 2, 2),   (')', 2, 3),  ('/', 2, 4),
            ('^',   3, 0), ('7', 3, 1),   ('8', 3, 2),   ('9', 3, 3),  ('*', 3, 4),
            ('√',   4, 0), ('4', 4, 1),   ('5', 4, 2),   ('6', 4, 3),  ('-', 4, 4),
            ('π',   5, 0), ('1', 5, 1),   ('2', 5, 2),   ('3', 5, 3),  ('+', 5, 4),
            ('e',   6, 0), ('0', 6, 1),   ('.', 6, 2),   ('=', 6, 3) 
        ]

        for (text, row, col) in buttons:
            colspan = 2 if text == '=' else 1
            btn = tk.Button(btns_frame, text=text, font=FONT_MAIN, bg=XP_BG, 
                            relief="raised", bd=2, command=lambda t=text: self.on_click(t))
            btn.grid(row=row, column=col, columnspan=colspan, sticky="nsew", padx=3, pady=3)

    # --- ENHANCED CONVERTER MODE ---
    def show_converter_mode(self):
        self.clear_container()
        self.lbl_desc.config(text="Universal Unit Conversion Engine")
        if self.sidebar_open: self.toggle_sidebar()

        container = tk.Frame(self.main_container, bg=XP_BG, padx=20, pady=20)
        container.pack(fill="both", expand=True)

        # Unit Data
        self.unit_cats = {
            "Weight": {"Gram (g)": 1, "Kg": 1000, "Lb": 453.592, "MilliLb (mLb)": 0.453592, "Ounce": 28.3495},
            "Volume": {"Milliliter (mL)": 1, "Liter (L)": 1000, "Cup": 236.588, "Gallon": 3785.41},
            "Length": {"Millimeter (mm)": 1, "Meter (m)": 1000, "Inch": 25.4, "Foot": 304.8}
        }

        tk.Label(container, text="Select Category:", bg=XP_BG).pack()
        self.cat_combo = ttk.Combobox(container, values=list(self.unit_cats.keys()))
        self.cat_combo.set("Weight")
        self.cat_combo.pack(fill="x", pady=5)
        self.cat_combo.bind("<<ComboboxSelected>>", self.update_units)

        tk.Label(container, text="From:", bg=XP_BG).pack()
        self.from_combo = ttk.Combobox(container)
        self.from_combo.pack(fill="x", pady=5)

        tk.Label(container, text="To:", bg=XP_BG).pack()
        self.to_combo = ttk.Combobox(container)
        self.to_combo.pack(fill="x", pady=5)

        tk.Label(container, text="Value:", bg=XP_BG).pack()
        self.conv_input = tk.Entry(container, font=FONT_DISPLAY)
        self.conv_input.pack(fill="x", pady=5)

        self.conv_res = tk.Label(container, text="Result: --", bg=XP_BG, font=FONT_DISPLAY, fg=XP_BLUE)
        self.conv_res.pack(pady=20)

        tk.Button(container, text="CONVERT", bg=XP_BLUE, fg="white", font=("Tahoma", 10, "bold"),
                  command=self.perform_conversion).pack(fill="x")
        
        self.update_units()

    def update_units(self, event=None):
        cat = self.cat_combo.get()
        units = list(self.unit_cats[cat].keys())
        self.from_combo['values'] = units
        self.to_combo['values'] = units
        self.from_combo.set(units[0])
        self.to_combo.set(units[1])

    def perform_conversion(self):
        try:
            cat = self.cat_combo.get()
            val = float(self.conv_input.get())
            # Convert to base unit then to target unit
            base_val = val * self.unit_cats[cat][self.from_combo.get()]
            final_val = base_val / self.unit_cats[cat][self.to_combo.get()]
            self.conv_res.config(text=f"Result: {round(final_val, 4)}")
        except:
            self.conv_res.config(text="Invalid Input")

    # --- PROGRAMMER MODE ---
    def show_programmer_mode(self):
        self.clear_container()
        self.lbl_desc.config(text="Base Conversion (Hex/Dec/Bin)")
        if self.sidebar_open: self.toggle_sidebar()
        
        p_frame = tk.Frame(self.main_container, bg=XP_BG, padx=20, pady=20)
        p_frame.pack(fill="both")

        tk.Label(p_frame, text="Enter Decimal Number:", bg=XP_BG).pack()
        dec_entry = tk.Entry(p_frame, font=FONT_DISPLAY)
        dec_entry.pack(fill="x", pady=5)

        res_txt = tk.StringVar(value="Hex: -\nBin: -\nOct: -")
        tk.Label(p_frame, textvariable=res_txt, bg=XP_WHITE, relief="sunken", font=("Courier New", 12), justify="left").pack(fill="x", pady=10, ipady=10)

        def convert_base():
            try:
                n = int(dec_entry.get())
                res_txt.set(f"Hex: {hex(n).upper()}\nBin: {bin(n)}\nOct: {oct(n)}")
            except: res_txt.set("Error: Enter a valid Integer")

        tk.Button(p_frame, text="CONVERT BASE", command=convert_base).pack(fill="x")

    # --- FINANCE MODE ---
    def show_finance_mode(self):
        self.clear_container()
        self.lbl_desc.config(text="Installation & Interest Calculator")
        if self.sidebar_open: self.toggle_sidebar()
        
        f_frame = tk.Frame(self.main_container, bg=XP_BG, padx=20, pady=20)
        f_frame.pack(fill="both")

        tk.Label(f_frame, text="Principal Amount:", bg=XP_BG).pack()
        p_ent = tk.Entry(f_frame); p_ent.pack(fill="x")
        
        tk.Label(f_frame, text="Rate (%) / Year:", bg=XP_BG).pack()
        r_ent = tk.Entry(f_frame); r_ent.pack(fill="x")
        
        tk.Label(f_frame, text="Time (Years):", bg=XP_BG).pack()
        t_ent = tk.Entry(f_frame); t_ent.pack(fill="x")

        res_lbl = tk.Label(f_frame, text="Total: --", font=FONT_DISPLAY, bg=XP_BG)
        res_lbl.pack(pady=10)

        def calc_finance():
            try:
                p, r, t = float(p_ent.get()), float(r_ent.get()), float(t_ent.get())
                total = p + (p * (r/100) * t)
                res_lbl.config(text=f"Total: {round(total, 2)}")
            except: res_lbl.config(text="Invalid Input")

        tk.Button(f_frame, text="CALCULATE TOTAL", command=calc_finance).pack(fill="x")

    # --- CORE CALCULATOR LOGIC ---
    def on_click(self, char):
        if char == 'C': self.expression = ""
        elif char == 'DEL': self.expression = self.expression[:-1]
        elif char == '=': self.expression = self.solve_expression(self.expression)
        elif char in ['sin', 'cos', 'tan', 'log', 'ln', '√']: self.expression += char + "("
        else: self.expression += str(char)
        self.equation.set(self.expression)

    def solve_expression(self, expr):
        try:
            calc_str = expr.replace('π', 'math.pi').replace('e', 'math.e').replace('^', '**')
            calc_str = calc_str.replace('√', 'math.sqrt').replace('ln(', 'math.log(')
            calc_str = calc_str.replace('log(', 'math.log10(').replace('sin(', 'math.sin(')
            calc_str = calc_str.replace('cos(', 'math.cos(').replace('tan(', 'math.tan(')
            result = eval(calc_str)
            return str(int(result)) if isinstance(result, float) and result.is_integer() else str(round(result, 8))
        except: return "Error"

    def bind_keys(self):
        self.root.bind("<Key>", self.handle_keypress)
        self.root.bind("<Return>", lambda e: self.on_click('='))
        self.root.bind("<BackSpace>", lambda e: self.on_click('DEL'))
        self.root.bind("<Escape>", lambda e: self.on_click('C'))

    def handle_keypress(self, event):
        if event.char in "0123456789+-*/.()^": self.on_click(event.char)

if __name__ == "__main__":
    root = tk.Tk()
    app = RetroScientificCalc(root)
    root.mainloop()
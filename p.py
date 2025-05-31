import tkinter as tk
from tkinter import ttk, messagebox
import random
import math

class DifferentialEquationsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Differential Equations Flashcard Game")
        self.root.geometry("800x600")
        self.root.configure(bg='#f0f0f0')
        
        # Game state
        self.current_card = 0
        self.score = 0
        self.total_attempts = 0
        self.streak = 0
        self.max_streak = 0
        self.show_answer = False
        self.show_steps = False
        
        # Card database with different difficulty levels - EXPANDED!
        self.cards = {
            'Basic': [
                {
                    'question': "What is the general form of a first-order linear differential equation?",
                    'answer': "dy/dx + P(x)y = Q(x)",
                    'steps': "This is the standard form where:\n• P(x) is the coefficient of y\n• Q(x) is the non-homogeneous term\n• If Q(x) = 0, the equation is homogeneous",
                    'type': 'definition'
                },
                {
                    'question': "Solve: dy/dx = 3x²",
                    'answer': "y = x³ + C",
                    'steps': "Step 1: Recognize this is direct integration\nStep 2: Integrate both sides: ∫dy = ∫3x² dx\nStep 3: y = 3∫x² dx = 3(x³/3) = x³ + C",
                    'type': 'integration'
                },
                {
                    'question': "What is the order of this DE: d²y/dx² + 3dy/dx + 2y = 0?",
                    'answer': "Second order (highest derivative is d²y/dx²)",
                    'steps': "Step 1: Identify all derivatives present: d²y/dx², dy/dx\nStep 2: Find the highest order derivative: d²y/dx² (second derivative)\nStep 3: The order equals the highest derivative order = 2",
                    'type': 'classification'
                },
                {
                    'question': "Solve: dy/dx = y",
                    'answer': "y = Ce^x",
                    'steps': "Step 1: Separate variables: dy/y = dx\nStep 2: Integrate both sides: ∫dy/y = ∫dx\nStep 3: ln|y| = x + C₁\nStep 4: |y| = e^(x + C₁) = e^C₁ · e^x\nStep 5: y = Ce^x where C = ±e^C₁",
                    'type': 'separable'
                },
                {
                    'question': "What makes a differential equation 'separable'?",
                    'answer': "It can be written as dy/dx = f(x)g(y), allowing separation of variables",
                    'steps': "A DE is separable when:\n• It can be written as dy/dx = f(x)g(y)\n• Variables can be separated: dy/g(y) = f(x)dx\n• Each side contains only one variable\n• Both sides can then be integrated independently",
                    'type': 'definition'
                },
                {
                    'question': "Solve: dy/dx = 2x",
                    'answer': "y = x² + C",
                    'steps': "Step 1: Recognize direct integration\nStep 2: Integrate both sides: ∫dy = ∫2x dx\nStep 3: y = 2∫x dx = 2(x²/2) = x² + C",
                    'type': 'integration'
                },
                {
                    'question': "What is the degree of this DE: (dy/dx)³ + 2y = x?",
                    'answer': "Third degree (highest power of the derivative is 3)",
                    'steps': "Step 1: Identify the highest order derivative: dy/dx\nStep 2: Find the highest power of this derivative: (dy/dx)³\nStep 3: The degree is the exponent: 3",
                    'type': 'classification'
                },
                {
                    'question': "Solve: dy/dx = -y/x",
                    'answer': "y = C/x or xy = C",
                    'steps': "Step 1: Separate variables: dy/y = -dx/x\nStep 2: Integrate both sides: ∫dy/y = ∫(-1/x)dx\nStep 3: ln|y| = -ln|x| + C₁\nStep 4: ln|y| + ln|x| = C₁\nStep 5: ln|xy| = C₁, so xy = C",
                    'type': 'separable'
                },
                {
                    'question': "What is an ordinary differential equation (ODE)?",
                    'answer': "A differential equation involving only one independent variable",
                    'steps': "ODE characteristics:\n• Contains one independent variable (usually x or t)\n• Contains one dependent variable (usually y)\n• All derivatives are ordinary derivatives (d/dx, not ∂/∂x)\n• Example: dy/dx + y = x (not ∂y/∂x + ∂y/∂t = 0)",
                    'type': 'definition'
                },
                {
                    'question': "Solve: dy/dx = e^x",
                    'answer': "y = e^x + C",
                    'steps': "Step 1: Recognize direct integration\nStep 2: Integrate both sides: ∫dy = ∫e^x dx\nStep 3: y = e^x + C",
                    'type': 'integration'
                },
                {
                    'question': "What does it mean for a DE to be 'linear'?",
                    'answer': "The dependent variable and all its derivatives appear to the first power only",
                    'steps': "A DE is linear when:\n• y and all derivatives (y', y'', etc.) have power 1\n• No products of y with its derivatives\n• No transcendental functions of y (sin(y), e^y, etc.)\n• Coefficients can be functions of x\nExample: y'' + 3y' + 2y = x is linear\nExample: yy' + y = x is NOT linear",
                    'type': 'definition'
                },
                {
                    'question': "Solve: dy/dx = sin(x)",
                    'answer': "y = -cos(x) + C",
                    'steps': "Step 1: Recognize direct integration\nStep 2: Integrate both sides: ∫dy = ∫sin(x) dx\nStep 3: y = -cos(x) + C",
                    'type': 'integration'
                },
                {
                    'question': "What is the difference between homogeneous and non-homogeneous DEs?",
                    'answer': "Homogeneous: all terms contain y or its derivatives. Non-homogeneous: has terms without y",
                    'steps': "Homogeneous DE: y'' + 3y' + 2y = 0\n• Every term contains y or a derivative\n• Right side equals zero\n\nNon-homogeneous DE: y'' + 3y' + 2y = x\n• Has terms without y (the 'forcing function')\n• Right side ≠ 0\n• Solution = homogeneous solution + particular solution",
                    'type': 'definition'
                },
                {
                    'question': "Solve: dy/dx = y²",
                    'answer': "y = -1/(x + C)",
                    'steps': "Step 1: Separate variables: dy/y² = dx\nStep 2: Rewrite: y⁻² dy = dx\nStep 3: Integrate: ∫y⁻² dy = ∫dx\nStep 4: -y⁻¹ = x + C₁\nStep 5: -1/y = x + C₁\nStep 6: y = -1/(x + C) where C = C₁",
                    'type': 'separable'
                },
                {
                    'question': "What is an initial value problem (IVP)?",
                    'answer': "A DE with specified values of the function at a particular point",
                    'steps': "An IVP consists of:\n• A differential equation: dy/dx = f(x,y)\n• Initial condition(s): y(x₀) = y₀\n• The solution must satisfy both the DE and initial condition\n• IVPs typically have unique solutions\nExample: dy/dx = y, y(0) = 2 → y = 2e^x",
                    'type': 'definition'
                },
                {
                    'question': "Solve: dy/dx = 1/x",
                    'answer': "y = ln|x| + C",
                    'steps': "Step 1: Recognize direct integration\nStep 2: Integrate both sides: ∫dy = ∫(1/x) dx\nStep 3: y = ln|x| + C\nNote: Absolute value needed since ln(x) undefined for x < 0",
                    'type': 'integration'
                },
                {
                    'question': "What is a partial differential equation (PDE)?",
                    'answer': "A differential equation involving partial derivatives with respect to multiple variables",
                    'steps': "PDE characteristics:\n• Multiple independent variables (x, y, t, etc.)\n• Contains partial derivatives (∂/∂x, ∂/∂y, etc.)\n• More complex than ODEs\nExample: ∂u/∂t = ∂²u/∂x² (heat equation)\nExample: ∂²u/∂x² + ∂²u/∂y² = 0 (Laplace equation)",
                    'type': 'definition'
                },
                {
                    'question': "Solve: dy/dx = cos(2x)",
                    'answer': "y = (1/2)sin(2x) + C",
                    'steps': "Step 1: Recognize direct integration\nStep 2: Integrate both sides: ∫dy = ∫cos(2x) dx\nStep 3: Use substitution u = 2x, du = 2dx\nStep 4: ∫cos(2x) dx = (1/2)∫cos(u) du = (1/2)sin(u) = (1/2)sin(2x)\nStep 5: y = (1/2)sin(2x) + C",
                    'type': 'integration'
                },
                {
                    'question': "What is the solution to dy/dx = 0?",
                    'answer': "y = C (constant function)",
                    'steps': "Step 1: If dy/dx = 0, then y has zero rate of change\nStep 2: Integrate: ∫dy = ∫0 dx\nStep 3: y = 0·x + C = C\nStep 4: y is constant for all x",
                    'type': 'basic'
                },
                {
                    'question': "Solve: dy/dx = xy",
                    'answer': "y = Ce^(x²/2)",
                    'steps': "Step 1: Separate variables: dy/y = x dx\nStep 2: Integrate both sides: ∫dy/y = ∫x dx\nStep 3: ln|y| = x²/2 + C₁\nStep 4: |y| = e^(x²/2 + C₁) = e^C₁ · e^(x²/2)\nStep 5: y = Ce^(x²/2) where C = ±e^C₁",
                    'type': 'separable'
                }
            ],
            'Intermediate': [
                {
                    'question': "Solve: dy/dx + 2y = 4e^(-2x)",
                    'answer': "y = (4x + C)e^(-2x)",
                    'type': 'linear_first_order'
                },
                {
                    'question': "Find the integrating factor for: dy/dx + 3y = x",
                    'answer': "μ(x) = e^(3x)",
                    'type': 'integrating_factor'
                },
                {
                    'question': "Solve: x dy/dx = y + x²",
                    'answer': "y = x(ln|x| + C)",
                    'type': 'homogeneous'
                },
                {
                    'question': "What is the characteristic equation for: d²y/dx² - 5dy/dx + 6y = 0?",
                    'answer': "r² - 5r + 6 = 0, which factors as (r-2)(r-3) = 0",
                    'type': 'characteristic'
                },
                {
                    'question': "Solve: d²y/dx² + 4y = 0",
                    'answer': "y = C₁cos(2x) + C₂sin(2x)",
                    'type': 'second_order_homogeneous'
                },
                {
                    'question': "Solve: dy/dx - y = x²",
                    'answer': "y = e^x(C - x² - 2x - 2)",
                    'type': 'linear_first_order'
                },
                {
                    'question': "Find the integrating factor for: x dy/dx + 2y = x³",
                    'answer': "μ(x) = x²",
                    'type': 'integrating_factor'
                },
                {
                    'question': "Solve: d²y/dx² - 3dy/dx + 2y = 0",
                    'answer': "y = C₁e^x + C₂e^(2x)",
                    'type': 'second_order_homogeneous'
                },
                {
                    'question': "What form does the particular solution take for: d²y/dx² + y = x²?",
                    'answer': "yₚ = ax² + bx + c (polynomial of same degree)",
                    'type': 'undetermined_coefficients'
                },
                {
                    'question': "Solve: dy/dx = (y - x)/(y + x)",
                    'answer': "Use substitution v = y/x: x² + y² = Cx",
                    'type': 'homogeneous'
                },
                {
                    'question': "Find the general solution: d²y/dx² + 9y = 0",
                    'answer': "y = C₁cos(3x) + C₂sin(3x)",
                    'type': 'second_order_homogeneous'
                },
                {
                    'question': "Solve: (x + y)dx + (x - y)dy = 0",
                    'answer': "x² + 2xy - y² = C",
                    'type': 'exact'
                },
                {
                    'question': "What is the particular solution form for d²y/dx² + y = e^x?",
                    'answer': "yₚ = Ae^x (exponential not in homogeneous solution)",
                    'type': 'undetermined_coefficients'
                },
                {
                    'question': "Solve: d²y/dx² - 4dy/dx + 4y = 0",
                    'answer': "y = (C₁ + C₂x)e^(2x) (repeated root r = 2)",
                    'type': 'repeated_roots'
                },
                {
                    'question': "Check if exact: (2x + y)dx + (x + 3y²)dy = 0",
                    'answer': "∂M/∂y = 1, ∂N/∂x = 1. Since they're equal, it's exact.",
                    'type': 'exact'
                },
                {
                    'question': "Solve: dy/dx + y/x = x",
                    'answer': "y = x²/3 + C/x",
                    'type': 'linear_first_order'
                },
                {
                    'question': "Find roots of characteristic equation: r² + 2r + 5 = 0",
                    'answer': "r = -1 ± 2i (complex conjugate roots)",
                    'type': 'characteristic'
                },
                {
                    'question': "What is the general solution for complex roots r = α ± βi?",
                    'answer': "y = e^(αx)[C₁cos(βx) + C₂sin(βx)]",
                    'type': 'complex_roots'
                },
                {
                    'question': "Solve: d²y/dx² + 2dy/dx + y = 0",
                    'answer': "y = (C₁ + C₂x)e^(-x) (repeated root r = -1)",
                    'type': 'repeated_roots'
                },
                {
                    'question': "For d²y/dx² + y = cos(x), what particular solution form do you try?",
                    'answer': "yₚ = x(A cos(x) + B sin(x)) (resonance case)",
                    'type': 'undetermined_coefficients'
                }
            ],
            'Advanced': [
                {
                    'question': "Solve using variation of parameters: d²y/dx² + y = sec(x)",
                    'answer': "y = C₁cos(x) + C₂sin(x) + sin(x)ln|sec(x) + tan(x)|",
                    'type': 'variation_of_parameters'
                },
                {
                    'question': "Find the general solution: d²y/dx² - 2dy/dx + y = e^x",
                    'answer': "y = (C₁ + C₂x)e^x + (x²/2)e^x",
                    'type': 'repeated_roots'
                },
                {
                    'question': "Solve the Bernoulli equation: dy/dx + y = xy³",
                    'answer': "Using substitution v = y^(-2): y = ±1/√(C·e^(-x²) - 1)",
                    'type': 'bernoulli'
                },
                {
                    'question': "What is the Wronskian of e^x and xe^x?",
                    'answer': "W = e^(2x)",
                    'type': 'wronskian'
                },
                {
                    'question': "Solve: (x² + y²)dx + 2xy dy = 0",
                    'answer': "x²y + y³/3 = C (exact equation)",
                    'type': 'exact'
                },
                {
                    'question': "Solve using variation of parameters: d²y/dx² - 2dy/dx + y = e^x/x",
                    'answer': "y = (C₁ + C₂x)e^x + e^x ln|x|",
                    'type': 'variation_of_parameters'
                },
                {
                    'question': "Solve the Bernoulli equation: x dy/dx + y = x²y³",
                    'answer': "Using v = y^(-2): y = ±1/√(Cx² + 2x³/3)",
                    'type': 'bernoulli'
                },
                {
                    'question': "Find the Wronskian of sin(x) and cos(x)",
                    'answer': "W = -1",
                    'type': 'wronskian'
                },
                {
                    'question': "Solve the Clairaut equation: y = xy' + (y')²",
                    'answer': "y = Cx + C² (general), y = -x²/4 (singular)",
                    'type': 'clairaut'
                },
                {
                    'question': "Solve using series: d²y/dx² + xy = 0 (Airy equation)",
                    'answer': "Power series solution around x = 0 with two linearly independent solutions",
                    'type': 'series'
                },
                {
                    'question': "Solve the Riccati equation: dy/dx = x² + y²",
                    'answer': "No elementary solution; requires special functions or numerical methods",
                    'type': 'riccati'
                },
                {
                    'question': "Find integrating factor for: (2x + y²)dx + (2xy - 3)dy = 0",
                    'answer': "μ(y) = e^(-3y/2) makes the equation exact",
                    'type': 'integrating_factor'
                },
                {
                    'question': "Solve: d²y/dx² + 4dy/dx + 4y = e^(-2x)ln(x)",
                    'answer': "Use variation of parameters with yₕ = (C₁ + C₂x)e^(-2x)",
                    'type': 'variation_of_parameters'
                },
                {
                    'question': "What is Green's function for d²y/dx² + y = δ(x)?",
                    'answer': "G(x,ξ) = sin(x-ξ)H(x-ξ) where H is Heaviside function",
                    'type': 'greens_function'
                },
                {
                    'question': "Solve the Euler equation: x²d²y/dx² + x dy/dx - y = 0",
                    'answer': "y = C₁x + C₂/x (using substitution x = e^t)",
                    'type': 'euler_equation'
                },
                {
                    'question': "Solve the Legendre equation: (1-x²)y'' - 2xy' + n(n+1)y = 0",
                    'answer': "Solutions are Legendre polynomials Pₙ(x) for integer n",
                    'type': 'special_functions'
                },
                {
                    'question': "Find the reduction of order for: d²y/dx² - 2dy/dx + y = 0 given y₁ = e^x",
                    'answer': "y₂ = xe^x (use v = y/y₁ substitution)",
                    'type': 'reduction_of_order'
                },
                {
                    'question': "Solve: d²y/dx² + x²y = 0 using Frobenius method",
                    'answer': "Power series solution with indicial equation and recurrence relations",
                    'type': 'frobenius'
                },
                {
                    'question': "What is the Abel's identity for second-order linear DEs?",
                    'answer': "W(x) = W(x₀)exp(-∫P(t)dt) where y'' + P(x)y' + Q(x)y = 0",
                    'type': 'abels_identity'
                },
                {
                    'question': "Solve the Bessel equation: x²y'' + xy' + (x² - n²)y = 0",
                    'answer': "Solutions are Bessel functions Jₙ(x) and Yₙ(x)",
                    'type': 'bessel_equation'
                }
            ]
        }
        
        self.current_difficulty = 'Basic'
        self.current_deck = self.cards[self.current_difficulty].copy()
        random.shuffle(self.current_deck)
        
        self.setup_ui()
        self.load_card()
        
    def setup_ui(self):
        # Title
        title_label = tk.Label(self.root, text="Differential Equations Flashcards", 
                              font=('Arial', 20, 'bold'), bg='#f0f0f0', fg='#333')
        title_label.pack(pady=20)
        
        # Difficulty selection
        difficulty_frame = tk.Frame(self.root, bg='#f0f0f0')
        difficulty_frame.pack(pady=10)
        
        tk.Label(difficulty_frame, text="Difficulty:", font=('Arial', 12), 
                bg='#f0f0f0').pack(side=tk.LEFT, padx=5)
        
        self.difficulty_var = tk.StringVar(value=self.current_difficulty)
        difficulty_menu = ttk.Combobox(difficulty_frame, textvariable=self.difficulty_var,
                                     values=['Basic', 'Intermediate', 'Advanced'],
                                     state='readonly', width=12)
        difficulty_menu.pack(side=tk.LEFT, padx=5)
        difficulty_menu.bind('<<ComboboxSelected>>', self.change_difficulty)
        
        # Score display
        self.score_frame = tk.Frame(self.root, bg='#f0f0f0')
        self.score_frame.pack(pady=10)
        
        self.score_label = tk.Label(self.score_frame, text=f"Score: {self.score}/{self.total_attempts}", 
                                   font=('Arial', 12), bg='#f0f0f0')
        self.score_label.pack(side=tk.LEFT, padx=20)
        
        self.streak_label = tk.Label(self.score_frame, text=f"Streak: {self.streak} (Best: {self.max_streak})", 
                                    font=('Arial', 12), bg='#f0f0f0')
        self.streak_label.pack(side=tk.LEFT, padx=20)
        
        # Card display
        self.card_frame = tk.Frame(self.root, bg='white', relief='raised', bd=2)
        self.card_frame.pack(pady=20, padx=40, fill='both', expand=True)
        
        # Card number
        self.card_number_label = tk.Label(self.card_frame, text="", font=('Arial', 10), 
                                         bg='white', fg='#666')
        self.card_number_label.pack(pady=5)
        
        # Question/Answer display
        self.question_label = tk.Label(self.card_frame, text="", font=('Arial', 14), 
                                      bg='white', wraplength=700, justify='center')
        self.question_label.pack(pady=20, padx=20, fill='both', expand=True)
        
        # Answer display (initially hidden)
        self.answer_label = tk.Label(self.card_frame, text="", font=('Arial', 12, 'italic'), 
                                    bg='white', fg='#0066cc', wraplength=700, justify='center')
        self.answer_label.pack(pady=10, padx=20)
        
        # Steps display (initially hidden)
        self.steps_label = tk.Label(self.card_frame, text="", font=('Arial', 10), 
                                   bg='#f8f9fa', fg='#495057', wraplength=700, justify='left',
                                   relief='sunken', bd=1)
        self.steps_label.pack(pady=5, padx=20, fill='x')
        
        # Control buttons
        button_frame = tk.Frame(self.root, bg='#f0f0f0')
        button_frame.pack(pady=20)
        
        self.show_answer_btn = tk.Button(button_frame, text="Show Answer", 
                                        command=self.toggle_answer, font=('Arial', 12),
                                        bg='#4CAF50', fg='white', padx=20, pady=5)
        self.show_answer_btn.pack(side=tk.LEFT, padx=10)
        
        self.show_steps_btn = tk.Button(button_frame, text="Show Steps", 
                                       command=self.toggle_steps, font=('Arial', 12),
                                       bg='#17a2b8', fg='white', padx=20, pady=5)
        self.show_steps_btn.pack(side=tk.LEFT, padx=5)
        
        self.correct_btn = tk.Button(button_frame, text="✓ Correct", 
                                    command=self.mark_correct, font=('Arial', 12),
                                    bg='#2196F3', fg='white', padx=20, pady=5, state='disabled')
        self.correct_btn.pack(side=tk.LEFT, padx=5)
        
        self.incorrect_btn = tk.Button(button_frame, text="✗ Incorrect", 
                                      command=self.mark_incorrect, font=('Arial', 12),
                                      bg='#f44336', fg='white', padx=20, pady=5, state='disabled')
        self.incorrect_btn.pack(side=tk.LEFT, padx=5)
        
        self.next_btn = tk.Button(button_frame, text="Next Card", 
                                 command=self.next_card, font=('Arial', 12),
                                 bg='#FF9800', fg='white', padx=20, pady=5, state='disabled')
        self.next_btn.pack(side=tk.LEFT, padx=10)
        
        # Study tools
        tools_frame = tk.Frame(self.root, bg='#f0f0f0')
        tools_frame.pack(pady=10)
        
        shuffle_btn = tk.Button(tools_frame, text="Shuffle Deck", 
                               command=self.shuffle_deck, font=('Arial', 10),
                               bg='#9C27B0', fg='white', padx=15, pady=3)
        shuffle_btn.pack(side=tk.LEFT, padx=5)
        
        reset_btn = tk.Button(tools_frame, text="Reset Stats", 
                             command=self.reset_stats, font=('Arial', 10),
                             bg='#607D8B', fg='white', padx=15, pady=3)
        reset_btn.pack(side=tk.LEFT, padx=5)
        
        hint_btn = tk.Button(tools_frame, text="Study Tip", 
                            command=self.show_study_tip, font=('Arial', 10),
                            bg='#795548', fg='white', padx=15, pady=3)
        hint_btn.pack(side=tk.LEFT, padx=5)
        
    def load_card(self):
        if self.current_card >= len(self.current_deck):
            self.end_deck()
            return
            
        card = self.current_deck[self.current_card]
        self.card_number_label.config(text=f"Card {self.current_card + 1} of {len(self.current_deck)} - {card['type'].replace('_', ' ').title()}")
        self.question_label.config(text=card['question'])
        self.answer_label.config(text="")
        self.steps_label.config(text="")
        
        self.show_answer = False
        self.show_steps = False
        self.show_answer_btn.config(text="Show Answer", state='normal')
        self.show_steps_btn.config(text="Show Steps", state='normal')
        self.correct_btn.config(state='disabled')
        self.incorrect_btn.config(state='disabled')
        self.next_btn.config(state='disabled')
        
    def toggle_answer(self):
        if not self.show_answer:
            card = self.current_deck[self.current_card]
            self.answer_label.config(text=f"Answer: {card['answer']}")
            self.show_answer_btn.config(text="Hide Answer")
            self.correct_btn.config(state='normal')
            self.incorrect_btn.config(state='normal')
            self.show_answer = True
        else:
            self.answer_label.config(text="")
            self.show_answer_btn.config(text="Show Answer")
            self.correct_btn.config(state='disabled')
            self.incorrect_btn.config(state='disabled')
            self.show_answer = False
            
    def toggle_steps(self):
        if not self.show_steps:
            card = self.current_deck[self.current_card]
            if 'steps' in card:
                self.steps_label.config(text=f"Solution Steps:\n{card['steps']}")
                self.show_steps_btn.config(text="Hide Steps")
                self.show_steps = True
            else:
                self.steps_label.config(text="No detailed steps available for this card.")
        else:
            self.steps_label.config(text="")
            self.show_steps_btn.config(text="Show Steps")
            self.show_steps = False
            
    def mark_correct(self):
        self.score += 1
        self.total_attempts += 1
        self.streak += 1
        self.max_streak = max(self.max_streak, self.streak)
        self.update_score_display()
        self.enable_next()
        
    def mark_incorrect(self):
        self.total_attempts += 1
        self.streak = 0
        self.update_score_display()
        self.enable_next()
        
    def enable_next(self):
        self.correct_btn.config(state='disabled')
        self.incorrect_btn.config(state='disabled')
        self.show_answer_btn.config(state='disabled')
        self.show_steps_btn.config(state='disabled')
        self.next_btn.config(state='normal')
        
    def next_card(self):
        self.current_card += 1
        self.load_card()
        
    def update_score_display(self):
        accuracy = (self.score / self.total_attempts * 100) if self.total_attempts > 0 else 0
        self.score_label.config(text=f"Score: {self.score}/{self.total_attempts} ({accuracy:.1f}%)")
        self.streak_label.config(text=f"Streak: {self.streak} (Best: {self.max_streak})")
        
    def change_difficulty(self, event=None):
        new_difficulty = self.difficulty_var.get()
        if new_difficulty != self.current_difficulty:
            self.current_difficulty = new_difficulty
            self.current_deck = self.cards[self.current_difficulty].copy()
            random.shuffle(self.current_deck)
            self.current_card = 0
            self.load_card()
            
    def shuffle_deck(self):
        remaining_cards = self.current_deck[self.current_card:]
        random.shuffle(remaining_cards)
        self.current_deck = self.current_deck[:self.current_card] + remaining_cards
        messagebox.showinfo("Shuffled", "Remaining cards have been shuffled!")
        
    def reset_stats(self):
        self.score = 0
        self.total_attempts = 0
        self.streak = 0
        self.max_streak = 0
        self.update_score_display()
        messagebox.showinfo("Reset", "Statistics have been reset!")
        
    def end_deck(self):
        accuracy = (self.score / self.total_attempts * 100) if self.total_attempts > 0 else 0
        message = f"""Deck Complete!
        
Final Score: {self.score}/{self.total_attempts} ({accuracy:.1f}%)
Best Streak: {self.max_streak}

Would you like to:
• Restart this deck
• Try a different difficulty
• Shuffle and restart"""
        
        result = messagebox.askyesno("Deck Complete", message + "\n\nRestart deck?")
        if result:
            self.current_card = 0
            random.shuffle(self.current_deck)
            self.load_card()
            
    def show_study_tip(self):
        tips = [
            "Tip: Always check if a DE is separable first - it's often the easiest method!",
            "Tip: For linear first-order DEs, find the integrating factor μ(x) = e^(∫P(x)dx)",
            "Tip: The characteristic equation method works for linear homogeneous DEs with constant coefficients",
            "Tip: When solving exact equations, check that ∂M/∂y = ∂N/∂x",
            "Tip: For repeated roots in characteristic equations, multiply by x for each repetition",
            "Tip: Variation of parameters is useful when the particular solution isn't obvious",
            "Tip: Always verify your solution by substituting back into the original equation!",
            "Tip: For complex roots α ± βi, the solution involves e^(αx)[cos(βx) and sin(βx)]",
            "Tip: Undetermined coefficients works when the non-homogeneous term has a finite derivative family",
            "Tip: Bernoulli equations can be linearized with the substitution v = y^(1-n)",
            "Tip: The Wronskian tells you if solutions are linearly independent (W ≠ 0)",
            "Tip: Green's functions are powerful for solving non-homogeneous boundary value problems",
            "Tip: Euler equations can be solved by substituting x = e^t",
            "Tip: Power series methods work well near ordinary points of the differential equation"
        ]
        tip = random.choice(tips)
        messagebox.showinfo("Study Tip", tip)

def main():
    root = tk.Tk()
    game = DifferentialEquationsGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
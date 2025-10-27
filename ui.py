import customtkinter

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")


class App(customtkinter.CTk):

    def __init__(self, submit_callback):
        
        super().__init__()

        self.submit_callback = submit_callback
        self.title("Laptop Recommendation Expert System")
        self.geometry("800x600")
        self.answers = {
            'primary_use': None,
            'budget': None,
            'portability': None,
            'battery': None,
            'features': [],
            'os': None
        }
        self.current_question = 0
        self.main_frame = customtkinter.CTkFrame(self)
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        self.title_label = customtkinter.CTkLabel(
            self.main_frame,
            text="💻 Laptop Recommendation Expert System",
            font=customtkinter.CTkFont(size=28, weight="bold")
        )
        self.title_label.pack(pady=(20, 30))

        self.question_container = customtkinter.CTkFrame(self.main_frame)
        self.question_container.pack(fill="both", expand=True, padx=20, pady=10)
        
        self.question_frames = []
        self.create_question_1()
        self.create_question_2()
        self.create_question_3()
        self.create_question_4()
        self.create_question_5()
        self.create_question_6()
        
        self.nav_frame = customtkinter.CTkFrame(self.main_frame)
        self.nav_frame.pack(pady=20)
        
        self.back_button = customtkinter.CTkButton(
            self.nav_frame,
            text="← Back",
            command=self.previous_question,
            width=120,
            state="disabled"
        )
        self.back_button.pack(side="left", padx=10)
        
        self.next_button = customtkinter.CTkButton(
            self.nav_frame,
            text="Next →",
            command=self.next_question,
            width=120
        )
        self.next_button.pack(side="left", padx=10)

        self.show_question(0)

    def create_question_1(self):
        frame = customtkinter.CTkFrame(self.question_container)
        
        question_label = customtkinter.CTkLabel(
            frame,
            text="What is your primary use for this laptop?",
            font=customtkinter.CTkFont(size=20, weight="bold")
        )
        question_label.pack(pady=(30, 20))
        
        self.q1_var = customtkinter.StringVar(value="general")
        
        options = [
            ("General use (browsing, documents, streaming)", "general"),
            ("Gaming", "gaming"),
            ("Creative/Professional work (video editing, design)", "creative"),
            ("School/University", "school")
        ]
        
        for text, value in options:
            radio = customtkinter.CTkRadioButton(
                frame,
                text=text,
                variable=self.q1_var,
                value=value,
                font=customtkinter.CTkFont(size=14)
            )
            radio.pack(pady=10, padx=40, anchor="w")
        
        self.question_frames.append(frame)

    def create_question_2(self):
        frame = customtkinter.CTkFrame(self.question_container)
        
        question_label = customtkinter.CTkLabel(
            frame,
            text="What is your budget range?",
            font=customtkinter.CTkFont(size=20, weight="bold")
        )
        question_label.pack(pady=(30, 20))
        
        self.q2_var = customtkinter.StringVar(value="midrange")
        
        options = [
            ("Under $600 (Economy)", "economy"),
            ("$600 - $1,200 (Mid-Range)", "midrange"),
            ("$1,200 - $1,800 (High-End)", "high-end"),
            ("$1,800+ (Unlimited)", "unlimited")
        ]
        
        for text, value in options:
            radio = customtkinter.CTkRadioButton(
                frame,
                text=text,
                variable=self.q2_var,
                value=value,
                font=customtkinter.CTkFont(size=14)
            )
            radio.pack(pady=10, padx=40, anchor="w")
        
        self.question_frames.append(frame)

    def create_question_3(self):
        frame = customtkinter.CTkFrame(self.question_container)
        
        question_label = customtkinter.CTkLabel(
            frame,
            text="How portable does your laptop need to be?",
            font=customtkinter.CTkFont(size=20, weight="bold")
        )
        question_label.pack(pady=(30, 20))
        
        self.q3_var = customtkinter.StringVar(value="occasional")
        
        options = [
            ("Stays on a desk (portability not important)", "desk"),
            ("Move it occasionally (room to room, home/office)", "occasional"),
            ("Carry it all day (commuting, travel)", "daily")
        ]
        
        for text, value in options:
            radio = customtkinter.CTkRadioButton(
                frame,
                text=text,
                variable=self.q3_var,
                value=value,
                font=customtkinter.CTkFont(size=14)
            )
            radio.pack(pady=10, padx=40, anchor="w")
        
        self.question_frames.append(frame)

    def create_question_4(self):
        frame = customtkinter.CTkFrame(self.question_container)
        
        question_label = customtkinter.CTkLabel(
            frame,
            text="How important is battery life to you?",
            font=customtkinter.CTkFont(size=20, weight="bold")
        )
        question_label.pack(pady=(30, 20))
        
        self.q4_var = customtkinter.StringVar(value="nice")
        
        options = [
            ("Not important (usually near a power outlet)", "not-important"),
            ("Nice to have (4-6 hours)", "nice"),
            ("All-day battery is critical (8+ hours)", "critical")
        ]
        
        for text, value in options:
            radio = customtkinter.CTkRadioButton(
                frame,
                text=text,
                variable=self.q4_var,
                value=value,
                font=customtkinter.CTkFont(size=14)
            )
            radio.pack(pady=10, padx=40, anchor="w")
        
        self.question_frames.append(frame)

    def create_question_5(self):
        frame = customtkinter.CTkFrame(self.question_container)
        
        question_label = customtkinter.CTkLabel(
            frame,
            text="Which features are important to you? (Select all that apply)",
            font=customtkinter.CTkFont(size=20, weight="bold")
        )
        question_label.pack(pady=(30, 20))
        
        info_label = customtkinter.CTkLabel(
            frame,
            text="Leave all unchecked if none are critical",
            font=customtkinter.CTkFont(size=12),
            text_color="gray"
        )
        info_label.pack(pady=(0, 20))
        
        self.q5_touchscreen = customtkinter.CTkCheckBox(
            frame,
            text="Touchscreen",
            font=customtkinter.CTkFont(size=14)
        )
        self.q5_touchscreen.pack(pady=10, padx=40, anchor="w")
        
        self.q5_numpad = customtkinter.CTkCheckBox(
            frame,
            text="Numeric Keypad",
            font=customtkinter.CTkFont(size=14)
        )
        self.q5_numpad.pack(pady=10, padx=40, anchor="w")
        
        self.q5_durability = customtkinter.CTkCheckBox(
            frame,
            text="Business-grade Durability",
            font=customtkinter.CTkFont(size=14)
        )
        self.q5_durability.pack(pady=10, padx=40, anchor="w")
        
        self.question_frames.append(frame)

    def create_question_6(self):
        frame = customtkinter.CTkFrame(self.question_container)
        
        question_label = customtkinter.CTkLabel(
            frame,
            text="Do you have an operating system preference?",
            font=customtkinter.CTkFont(size=20, weight="bold")
        )
        question_label.pack(pady=(30, 20))
        
        self.q6_var = customtkinter.StringVar(value="no-preference")
        
        options = [
            ("Windows", "windows"),
            ("macOS", "macos"),
            ("No Preference", "no-preference")
        ]
        
        for text, value in options:
            radio = customtkinter.CTkRadioButton(
                frame,
                text=text,
                variable=self.q6_var,
                value=value,
                font=customtkinter.CTkFont(size=14)
            )
            radio.pack(pady=10, padx=40, anchor="w")
        
        self.question_frames.append(frame)

    def show_question(self, index):
        for frame in self.question_frames:
            frame.pack_forget()
        if 0 <= index < len(self.question_frames):
            self.question_frames[index].pack(fill="both", expand=True)
            self.current_question = index
            if index == 0:
                self.back_button.configure(state="disabled")
            else:
                self.back_button.configure(state="normal")
            
            if index == len(self.question_frames) - 1:
                self.next_button.configure(text="Get Recommendation ✓")
            else:
                self.next_button.configure(text="Next →")

    def next_question(self):
        if self.current_question < len(self.question_frames) - 1:
            self.show_question(self.current_question + 1)
        else:
            self.submit_answers()

    def previous_question(self):
        if self.current_question > 0:
            self.show_question(self.current_question - 1)

    def get_answers(self):
        features = []
        if self.q5_touchscreen.get():
            features.append("touchscreen")
        if self.q5_numpad.get():
            features.append("numpad")
        if self.q5_durability.get():
            features.append("durability")
        
        answers = {
            'primary_use': self.q1_var.get(),
            'budget': self.q2_var.get(),
            'portability': self.q3_var.get(),
            'battery': self.q4_var.get(),
            'features': features,
            'os': self.q6_var.get()
        }
        
        return answers

    def submit_answers(self):
        self.answers = self.get_answers()
        if self.submit_callback:
            self.submit_callback(self.answers)

    def show_recommendation(self, reco_data):
        self.question_container.pack_forget()
        self.nav_frame.pack_forget()

        self.results_frame = customtkinter.CTkFrame(self.main_frame)
        self.results_frame.pack(fill="both", expand=True, padx=20, pady=10)

        results_title = customtkinter.CTkLabel(
            self.results_frame,
            text="Your Recommendation",
            font=customtkinter.CTkFont(size=24, weight="bold"),
            text_color="#4A9EFF"
        )
        results_title.pack(pady=(30, 20))
        recommendation_label = customtkinter.CTkLabel(
            self.results_frame,
            text=reco_data.get('recommendation', 'Budget All-Rounder'),
            font=customtkinter.CTkFont(size=32, weight="bold"),
            text_color="#FFFFFF"
        )
        recommendation_label.pack(pady=(10, 20))
        divider = customtkinter.CTkFrame(self.results_frame, height=2, fg_color="#4A9EFF")
        divider.pack(fill="x", padx=100, pady=10)
        reason_title = customtkinter.CTkLabel(
            self.results_frame,
            text="Why this recommendation?",
            font=customtkinter.CTkFont(size=16, weight="bold"),
            text_color="#A0A0A0"
        )
        reason_title.pack(pady=(20, 10))
        
        reason_label = customtkinter.CTkLabel(
            self.results_frame,
            text=reco_data.get('reason', 'A versatile option for your needs.'),
            font=customtkinter.CTkFont(size=14),
            wraplength=600,
            justify="center"
        )
        reason_label.pack(pady=(0, 20))
        models_title = customtkinter.CTkLabel(
            self.results_frame,
            text="Recommended Models:",
            font=customtkinter.CTkFont(size=16, weight="bold"),
            text_color="#A0A0A0"
        )
        models_title.pack(pady=(20, 10))
        
        models_label = customtkinter.CTkLabel(
            self.results_frame,
            text=reco_data.get('models', 'Various models available'),
            font=customtkinter.CTkFont(size=14),
            wraplength=600,
            justify="center",
            text_color="#4A9EFF"
        )
        models_label.pack(pady=(0, 30))
        start_over_button = customtkinter.CTkButton(
            self.results_frame,
            text="🔄 Start Over",
            command=self.reset_app,
            font=customtkinter.CTkFont(size=16, weight="bold"),
            width=200,
            height=40
        )
        start_over_button.pack(pady=20)

    def reset_app(self):
        if hasattr(self, 'results_frame'):
            self.results_frame.destroy()
        self.q1_var.set("general")
        self.q2_var.set("midrange")
        self.q3_var.set("occasional")
        self.q4_var.set("nice")
        self.q5_touchscreen.deselect()
        self.q5_numpad.deselect()
        self.q5_durability.deselect()
        self.q6_var.set("no-preference")
        self.question_container.pack(fill="both", expand=True, padx=20, pady=10)
        self.nav_frame.pack(pady=20)
        self.show_question(0)

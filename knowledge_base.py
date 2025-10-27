from experta import KnowledgeEngine, Rule, Fact, DefFacts, MATCH, TEST


class LaptopKnowledgeEngine(KnowledgeEngine):

    @DefFacts()
    def initial_facts(self):
        yield Fact(laptop_type="Ultrabook", 
                  description="Thin, light, premium laptops with excellent battery life")
        yield Fact(laptop_type="Gaming Laptop", 
                  description="High-performance laptops with dedicated graphics")
        yield Fact(laptop_type="2-in-1 Convertible", 
                  description="Versatile laptops with touchscreen and flexible form factors")
        yield Fact(laptop_type="Budget All-Rounder", 
                  description="Affordable, general-purpose laptops")
        yield Fact(laptop_type="Professional Workstation", 
                  description="Enterprise-grade laptops built for reliability and performance")

    # Rule 1: Gaming Enthusiast
    @Rule(
        Fact(primary_use="gaming"),
        Fact(budget=MATCH.budget),
        TEST(lambda budget: budget in ["high-end", "unlimited"]),
        salience=10
    )
    def gaming_recommendation(self, budget):
        self.declare(Fact(
            recommendation="Gaming Laptop",
            reason="You need high performance for gaming. Gaming laptops offer powerful GPUs and high refresh rate displays.",
            models="ASUS ROG Zephyrus G14, MSI Raider GE78, Alienware m16"
        ))

    # Rule 2: Student Note-Taker (Touchscreen Priority)
    @Rule(
        Fact(primary_use="school"),
        Fact(features=MATCH.features),
        TEST(lambda features: "touchscreen" in features),
        salience=10
    )
    def student_touchscreen_recommendation(self, features):
        self.declare(Fact(
            recommendation="2-in-1 Convertible",
            reason="Perfect for note-taking and flexible learning. Touchscreen and stylus support enhance productivity.",
            models="HP Spectre x360, Lenovo Yoga 9i, Microsoft Surface Pro 9"
        ))

    # Rule 3: Student Commuter (Portability + Battery)
    @Rule(
        Fact(primary_use="school"),
        Fact(portability="daily"),
        Fact(battery="critical")
    )
    def student_portable_recommendation(self):
        self.declare(Fact(
            recommendation="Ultrabook",
            reason="Best for students who carry their laptop daily. Lightweight with all-day battery life.",
            models="Dell XPS 13, Apple MacBook Air M3, ASUS ZenBook 14"
        ))

    # Rule 4: Professional Creative Work
    @Rule(
        Fact(primary_use="creative"),
        Fact(budget="unlimited")
    )
    def creative_professional_recommendation(self):
        self.declare(Fact(
            recommendation="Professional Workstation",
            reason="Creative work demands color-accurate displays and powerful processing. Workstations deliver professional-grade performance.",
            models="Apple MacBook Pro 16, Dell XPS 15, HP ZBook Studio G10"
        ))

    # Rule 5: macOS User
    @Rule(Fact(os="macos"), salience=10)
    def mac_user_recommendation(self):
        self.declare(Fact(
            recommendation="Ultrabook",
            reason="macOS is only available on Apple laptops. MacBooks offer premium build quality and seamless ecosystem integration.",
            models="MacBook Air M3, MacBook Pro 14 M3, MacBook Pro 16 M3"
        ))

    # Rule 6: Economy Budget User
    @Rule(Fact(budget="economy"))
    def economy_budget_recommendation(self):
        self.declare(Fact(
            recommendation="Budget All-Rounder",
            reason="Great value for everyday tasks like browsing, documents, and streaming without breaking the bank.",
            models="Acer Aspire 5, HP Pavilion 15, Lenovo IdeaPad 3"
        ))

    # Rule 7: Desk-Bound User
    @Rule(Fact(portability="desk"))
    def desk_user_recommendation(self):
        self.declare(Fact(
            recommendation="Budget All-Rounder",
            reason="Since portability isn't a concern, you can get larger screens and better value for money.",
            models="HP Pavilion 17, Acer Aspire 5 17-inch, Dell Inspiron 17"
        ))

    # Rule 8: Business Durability Focus
    @Rule(
        Fact(features=MATCH.features),
        TEST(lambda features: "durability" in features),
        salience=5
    )
    def business_durability_recommendation(self, features):
        self.declare(Fact(
            recommendation="Professional Workstation",
            reason="Business-grade laptops offer military-spec durability, enterprise support, and extended warranties.",
            models="Lenovo ThinkPad T14, HP EliteBook 840 G10, Dell Latitude 7440"
        ))

    # Rule 9: Premium General Use
    @Rule(
        Fact(primary_use="general"),
        Fact(budget="high-end")
    )
    def premium_general_recommendation(self):
        self.declare(Fact(
            recommendation="Ultrabook",
            reason="Premium ultrabooks offer the best all-around experience with exceptional build quality and performance.",
            models="Dell XPS 13 Plus, HP Spectre x360, LG Gram 16"
        ))

    # Rule 10: Mid-Range General Use
    @Rule(
        Fact(primary_use="general"),
        Fact(budget="midrange")
    )
    def midrange_general_recommendation(self):
        self.declare(Fact(
            recommendation="Budget All-Rounder",
            reason="Perfect balance of performance and value for everyday computing tasks.",
            models="ASUS VivoBook 15, Lenovo IdeaPad Slim 5, HP Pavilion 14"
        ))

    # Rule 11: Creative Work on Budget
    @Rule(
        Fact(primary_use="creative"),
        Fact(budget=MATCH.budget),
        TEST(lambda budget: budget in ["economy", "midrange"])
    )
    def budget_creative_recommendation(self, budget):
        self.declare(Fact(
            recommendation="Budget All-Rounder",
            reason="While not ideal for intensive creative work, these offer good value with decent performance for lighter tasks.",
            models="ASUS VivoBook Pro 15, Acer Swift X, HP Pavilion Plus 14"
        ))

    # Rule 12: Default Fallback (Lowest Priority)
    @Rule(salience=-1)
    def default_recommendation(self):
        self.declare(Fact(
            recommendation="Budget All-Rounder",
            reason="A versatile, affordable option suitable for most everyday computing needs.",
            models="Acer Aspire 5, Lenovo IdeaPad 3, HP 15"
        ))

    def get_recommendation(self):
        for fact in self.facts.values():
            if isinstance(fact, Fact) and 'recommendation' in fact:
                return {
                    'recommendation': fact.get('recommendation'),
                    'reason': fact.get('reason'),
                    'models': fact.get('models')
                }
        return None

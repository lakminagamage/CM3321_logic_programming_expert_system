from experta import Fact
from knowledge_base import LaptopKnowledgeEngine
from ui import App


class LaptopRecommendationSystem:

    def __init__(self):
        """Initialize the recommendation system."""
        self.engine = LaptopKnowledgeEngine()
        self.app = None

    def run_expert_system(self, answers_dict):
        self.engine.reset()
        for key, value in answers_dict.items():
            if key == 'features':
                if value:
                    self.engine.declare(Fact(features=value))
            elif key == 'os' and value != 'no-preference':
                self.engine.declare(Fact(os=value))
            elif value:
                self.engine.declare(Fact(**{key: value}))
        
        self.engine.run()
        recommendation = self.engine.get_recommendation()

        if recommendation:
            self.app.show_recommendation(recommendation)
        else:
            self.app.show_recommendation({
                'recommendation': 'Budget All-Rounder',
                'reason': 'A versatile option suitable for most everyday computing needs.',
                'models': 'Acer Aspire 5, Lenovo IdeaPad 3, HP 15'
            })

    def start(self):
        self.app = App(submit_callback=self.run_expert_system)
        
        self.app.mainloop()


def main():
    system = LaptopRecommendationSystem()
    system.start()


if __name__ == "__main__":
    main()

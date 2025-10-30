from experta import Fact
from knowledge_base import LaptopKnowledgeEngine
from ui import App


class LaptopRecommendationSystem:
    """
    Main orchestrator class that connects the UI with the expert system engine.
    """

    def __init__(self):
        self.engine = LaptopKnowledgeEngine()
        self.app = None

    def run_expert_system(self, answers_dict):
        """
        Process user answers through the expert system and display results.
        """
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
        """
        Start the application by initializing and launching the GUI.
        """
        self.app = App(submit_callback=self.run_expert_system)
        
        self.app.mainloop()


def main():
    """
    Main entry point of the application.
    """
    system = LaptopRecommendationSystem()
    system.start()


if __name__ == "__main__":
    main()

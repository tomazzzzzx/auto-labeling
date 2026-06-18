class AutoLabeler:
    def __init__(self, llm): self.llm = llm
    def label_batch(self, texts, task):
        return [self.llm(f"Task: {task}\nText: {t}\nLabel:") for t in texts]

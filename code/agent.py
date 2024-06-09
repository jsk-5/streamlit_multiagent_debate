


class Agent:
    def __init__(self, model_name: str, name: str, temperature: float, llm) -> None:
        """Create an agent

        Args:
            model_name(str): model name
            name (str): name of this agent
            temperature (float): higher values make the output more random, while lower values make it more focused and deterministic
            sleep_time (float): sleep because of rate limits
        """
        self.model_name = model_name
        self.name = name
        self.temperature = temperature
        self.llm = llm 
        self.langchain = None
        


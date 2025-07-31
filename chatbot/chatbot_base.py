class ChatbotBase:
    """
    Base class defining the structure and interface for all chatbot implementations.
    """

    def __init__(self, name: str = "Chatbot") -> None:
        self.name = name
        self.conversation_is_active = True

    def greeting(self) -> None:
        print(f'Hello I am {self.name}')

    def farewell(self) -> None:
        print('Goodbye!')

    def is_conversation_active(self) -> bool:
        """
        Check whether the conversation is still active.
        """
        return self.is_conversation_active

    def receive_input(self) -> str:
        return input()

    def process_input(self, user_input: str) -> str:
        raise NotImplementedError('process_input() not implemented')

    def generate_response(self, processed_input: str) -> str:
        raise NotImplementedError('generate_response() not implemented')

    def respond(self, out_message: str = None) -> str:
        if isinstance(out_message, str):
            print(out_message)
        received_input = self.receive_input()
        processed_input = self.process_input(received_input)
        response = self.generate_response(processed_input)
        return response
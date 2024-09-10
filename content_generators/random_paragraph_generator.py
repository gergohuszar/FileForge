import random
from faker import Faker


class ParagraphGenerator:
    def __init__(self, faker_instance=None):
        """
        Initialize the ParagraphGenerator class.

        Args:
            faker_instance (Faker, optional): An optional Faker instance to allow custom behavior.
        """

        if faker_instance:
            if not isinstance(faker_instance, Faker):
                raise ValueError('Parameter faker_instance must be an instance of Faker')
            
            self.fake = faker_instance
        else:
            self.fake = Faker()

    def _insert_pii_and_context(
        self, paragraph: str, pii: str, context_words: list[str]
    ) -> str:
        """
        Insert the PII and context words into the paragraph at random positions.
        """
        if not paragraph or not isinstance(paragraph, str):
            raise ValueError('Parameter paragraph must be a str')
        
        if not pii or not isinstance(pii, str):
            raise ValueError('Parameter pii must be a str')
        
        if not context_words or not isinstance(context_words, list):
            raise ValueError('Parameter context_words must be a list[str]')

        paragraph_words = paragraph.split()
        random_place_in_paragraph = random.randint(0, len(paragraph_words) - 1)
        paragraph_words.insert(random_place_in_paragraph, pii)

        # Insert context words near the PII
        for context in context_words:
            # Find the index of the PII to place the context near it
            template_word_i: int = paragraph_words.index(pii)

            # Calculate a position nearby the PII, ensuring it's within bounds
            delta: int = random.randint(-4, 4)
            context_i = max(0, min(template_word_i + delta, len(paragraph_words) - 1))

            paragraph_words.insert(context_i, context)

        modified_paragraph = " ".join(paragraph_words)
        return modified_paragraph

    def generate_with_random_choice_of_piis(
        self, piis: list[str], context_words: list[str], num_of_sentences: int
    ) -> str:
        """
        Generate a paragraph with a given number of sentences,
        and randomly insert a PII and context words.

        Args:
            piis (list): List of personally identifiable information (PII).
            context_words (list): List of words to insert around the PII.
            num_of_sentences (int): The number of sentences for the paragraph.

        Returns:
            str: A paragraph with PII and context words inserted.
        """

        if not piis or not isinstance(piis, list):
            raise ValueError("Parameter piis must be a non-empty list[str]")
        
        if not context_words or not isinstance(context_words, list):
            raise ValueError("Parameter context_words must be a non-empty list[str]")
        
        if not num_of_sentences or not isinstance(num_of_sentences, int):
            raise ValueError("Parameter num_of_sentences must be a non-empty list[str]")


        # Select 2-4 random context words
        random_contexts = random.sample(
            context_words, random.randint(2, min(4, len(context_words)))
        )

        # Select a random PII
        random_pii = random.choice(piis)

        return self.generate_for_pii(pii=random_pii, context_words=random_contexts, num_of_sentences=num_of_sentences)

    
    def generate_for_pii(self, pii: str, context_words: list[str], num_of_sentences: int) -> str:
        if not pii or not isinstance(pii, str):
            raise ValueError("Parameter pii must be a non-empty str")
        
        if not context_words or not isinstance(context_words, list):
            raise ValueError("Parameter context_words must be a non-empty list[str]")
        
        if not num_of_sentences or not isinstance(num_of_sentences, int) or num_of_sentences <= 0:
            raise ValueError('Parameter num_of_sentences must be an int, greater than 0!')

        # Generate a random paragraph
        paragraph: str = self.fake.paragraph(num_of_sentences)

        # Insert the PII and context words into the paragraph
        updated_paragraph = self._insert_pii_and_context(paragraph=paragraph, pii=pii, context_words=context_words)
        return updated_paragraph
    

    def generate_for_all_piis(self, piis: list[str], context_words: list[str], num_of_sentences: int) -> list[str]:
        return [self.generate_for_pii(pii=pii, context_words=context_words, num_of_sentences=num_of_sentences) for pii in piis]
        

import random
from faker import Faker


class ParagraphGenerator:
    def __init__(self, faker_instance=None):
        """
        Initialize the ParagraphGenerator class.

        Args:
            faker_instance (Faker, optional): An optional Faker instance to allow custom behavior.
        """
        self.fake = Faker()

    def _insert_pii_and_context(
        self, paragraph_words: list[str], random_pii: str, context_words: list[str]
    ) -> list[str]:
        """
        Insert the PII and context words into the paragraph at random positions.
        """
        random_place_in_paragraph = random.randint(0, len(paragraph_words) - 1)
        paragraph_words.insert(random_place_in_paragraph, random_pii)

        # Insert context words near the PII
        for context in context_words:
            # Find the index of the PII to place the context near it
            template_word_i: int = paragraph_words.index(random_pii)

            # Calculate a position nearby the PII, ensuring it's within bounds
            delta: int = random.randint(-4, 4)
            context_i = max(0, min(template_word_i + delta, len(paragraph_words) - 1))

            paragraph_words.insert(context_i, context)

        return paragraph_words

    def generate_paragraph(
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
        # Handle edge cases where piis or context_words are empty
        if not piis or not context_words:
            raise ValueError("PII list and context words must not be empty")

        # Select 2-4 random context words
        random_contexts = random.sample(
            context_words, random.randint(2, min(4, len(context_words)))
        )

        # Select a random PII
        random_pii = random.choice(piis)

        # Generate a random paragraph
        paragraph: str = self.fake.paragraph(num_of_sentences)
        words = paragraph.split()

        # Insert the PII and context words into the paragraph
        updated_words = self._insert_pii_and_context(words, random_pii, random_contexts)

        return " ".join(updated_words)

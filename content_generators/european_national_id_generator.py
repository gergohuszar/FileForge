import random
import itertools
from .random_paragraph_generator import ParagraphGenerator


class EuropeanNationalIdGenerator:
    _GERMAN_IDS = [
        "LZ6311T47",
        "T22000129",
        "T602301F1",
        "L5MF2G2XV",
    ]

    _FRENCH_IDS = [
        "X4RTBPFW4",
        "T7X62TZ79",
        "678456789345",
        "060631305008"
    ]

    _SPANISH_IDS = [
        "53505506P",
        "AAA001424",
        "423886043",
        "53578667Y"
    ]

    _PORTUGUESE_IDS = [
        "426349253<ZY8",
        "118666070",
        "62843870",
    ]

    _ITALIAN_IDS = [
        "CA00000AA",
        "CA21067AA",
    ]

    _CONTEXT_WORDS = [
        'ID',
        'my ID',
        'your ID',
        'new ID',
        'old ID',
        'EU ID',
        'number',
        'national',
        'NIN',
        'identification',
        'identity',
        'personal',
    ]

    # Some rules for european national id card numbers:
    #   - Variable length from 9-14 characters
    #   - Can contain alphanumeric characters:
    #     - A-Z
    #     - 0-9
    #     - '<' character
    #   - EU member countries themselves define the structure of the card number
    CHARACTERS_ALLOWED = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789<'
    ID_NUMBER_LENGTH_MIN = 9
    ID_NUMBER_LENGTH_MAX = 14

    def _generate_random_id_number(self):
        len = random.randint(self.ID_NUMBER_LENGTH_MIN, self.ID_NUMBER_LENGTH_MAX)
        return ''.join([random.choice(self.CHARACTERS_ALLOWED) for _ in range(len)])
    
    def generate_all_predefined(self, num_of_paragraph_sentences: int) -> list[str]:
        paragraph_generator = ParagraphGenerator()

        return itertools.chain(
            paragraph_generator.generate_for_all_piis(piis=self._GERMAN_IDS, context_words=self._CONTEXT_WORDS, num_of_sentences=num_of_paragraph_sentences),
            paragraph_generator.generate_for_all_piis(piis=self._FRENCH_IDS, context_words=self._CONTEXT_WORDS, num_of_sentences=num_of_paragraph_sentences),
            paragraph_generator.generate_for_all_piis(piis=self._SPANISH_IDS, context_words=self._CONTEXT_WORDS, num_of_sentences=num_of_paragraph_sentences),
            paragraph_generator.generate_for_all_piis(piis=self._PORTUGUESE_IDS, context_words=self._CONTEXT_WORDS, num_of_sentences=num_of_paragraph_sentences),
            paragraph_generator.generate_for_all_piis(piis=self._ITALIAN_IDS, context_words=self._CONTEXT_WORDS, num_of_sentences=num_of_paragraph_sentences),
        )

    def generate_random_ids(self, num_of_random_piis: int, num_of_paragraph_sentences: int) -> list[str]:
        paragraph_generator = ParagraphGenerator()

        random_piis = [self._generate_random_id_number() for _ in range(num_of_random_piis)]
        return paragraph_generator.generate_for_all_piis(piis=random_piis, context_words=self._CONTEXT_WORDS, num_of_sentences=num_of_paragraph_sentences)


    

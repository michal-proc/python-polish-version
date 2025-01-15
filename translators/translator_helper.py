import yaml


class TranslatorHelper:

    @staticmethod
    def translate_identifier(identifier):
        with open("identifiers.yml", "r") as file:
            identifiers = yaml.safe_load(file)

        return identifiers.get(identifier, identifier)

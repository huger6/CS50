from datetime import date, datetime
import sys
import re
import operator
import inflect

class Minutes:
    def __init__(self, birth):
        if not self.isvalid(birth):
            sys.exit("Invalid date")
        self.birth = datetime.strptime(birth, "%Y-%m-%d").date()
        self.todays_date = date.today()

    #Verificar data
    def isvalid(self, value):
        pattern = r"^(?:19|20)\d\d-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$"
        if matches := re.match(pattern, value):
            return True
        else:
            return False
    #Subtrair ano de nascimento ao atual e passar para minutos
    def __sub__(self):
        delta = self.todays_date - self.birth
        return delta.days * 24 * 60

    def __str__(self):
        minutes = self.__sub__()
        p = inflect.engine()
        minutes_words = p.number_to_words(minutes)
        if " and" in minutes_words:
            minutes_words = minutes_words.replace(" and", "")
        return minutes_words.capitalize()

def main():
    birth = input("Date of Birth: ").strip()
    minutes_instance = Minutes(birth)
    print(f"{minutes_instance} minutes")

if __name__ == "__main__":
    main()

#6. Агрегація словника: сума значень у словнику за ключем.
salary={"Oleh" : [10, 12, 13, 10, 10, 15],
        "Dima" : [15, 15, 15, 15, 20, 20],
        "Alina" : [19, 15, 15, 15, 20, 10],
        "Mariia" : [10, 25, 21, 10, 11, 5]
}
print(f"Your salary is",sum(salary["Alina"]), "thousand")

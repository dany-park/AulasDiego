'''#cadastro hospital

nome1 = input("Qual o nome do paciente?")
sobrenome1 = input("E o sobrenome?")

nome2 = input("Qual o nome do paciente?")
sobrenome2 = input("E o sobrenome?")

nome3 = input("Qual o nome do paciente?")
sobrenome3 = input("E o sobrenome?")

print(f"Os pacientes são: \n {nome1} {sobrenome1} \n {nome2} {sobrenome2} \n {nome3} {sobrenome3}")'''

pacientes = []
numero_repeticoes = int(input("Quanto pacientes voce quer cadastrar?"))

for i in range(numero_repeticoes):
    paciente = {"nome":input("Qual o nome do paciente?"),
            "sobrenome":input("E o sobrenome?")}
    pacientes.append(paciente)

print("Os pacientes são:")
for nome_completo in pacientes:
    print(nome_completo.get("nome"), nome_completo.get("sobrenome"))








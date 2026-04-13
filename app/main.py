from chatbot import responder

print("💬 BIA Financeira iniciada (digite 'sair')")

while True:
    msg = input("Você: ")

    if msg.lower() == "sair":
        break

    print("BIA:", responder(msg))

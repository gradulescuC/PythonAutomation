import psutil  # utitar care ne permite sa avem un view catre partea de performance testing


def get_memory():
    return psutil.virtual_memory().percent


memory = get_memory()
print(memory)


def memory_logger(msg):
    def logger():
        print(f"Logging memory data {msg}.")

        def another_logger():
            print("Just checking nested functions")

        another_logger()

    logger()


memory_logger(memory)


# -----------------------------------------------------

def closure_memory_logger(msg):
    threshold = 90

    def logger():
        print(f"Logging memory data with closure {msg}, keep an eye to the threshold {threshold}")

    return logger


print("----------------------------")

# cl = closure_memory_logger(memory)
closure_memory_logger(memory)()
# print(cl)
# cl()


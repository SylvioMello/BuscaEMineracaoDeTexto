config_file = "GLI.CFG"
cfg_path = "../BasesTrabalhoIndividual/" + config_file
with open(cfg_path, "r") as config_file:
    first_line = config_file.readline()
    if first_line == "STEMMER\n":
        print('hi')
        stemmer = True
    else:
        print('hello')
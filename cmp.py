import json

# Couleurs ANSI
ORANGE = "\033[38;5;214m"
VERT = "\033[32m"
BLEU_CLAIR = "\033[94m"
ROSE = "\033[0;35m"
RESET = "\033[0m"


def compare_json(f1_path, f2_path):
    with open(f1_path, "r", encoding="utf-8") as f:
        j1 = json.load(f)["colors"]
    with open(f2_path, "r", encoding="utf-8") as f:
        j2 = json.load(f)["colors"]

    # Ensemble de tous les champs
    all_keys = set(j1.keys()) | set(j2.keys())

    for key in sorted(all_keys):
        if key not in j2:
            print(f"{ORANGE}Champs disparu : {key}{RESET}")
        elif key not in j1:
            # print(f"{VERT}Champs ajouté : {key}{RESET}")
            print(f"- `{key}`")
        else:
            if j1[key] != j2[key]:
                if j1[key] == "#FF00FF":
                    # print(f"{ROSE}Champs ajouté : {key}{RESET}")
                    print(f"- `{key}`")
                else:
                    # print(
                    # f"{BLEU_CLAIR}Champs modifié : {key} — {j1[key]} -> {j2[key]}{RESET}"
                    # f"- `{key}`"
                    # )
                    pass
            else:
                # Champ inchangé : ne rien afficher
                pass


if __name__ == "__main__":
    compare_json("themes/OLD.json", "themes/Osmoz-dark-color-theme.json")

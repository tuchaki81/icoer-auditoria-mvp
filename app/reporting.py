def generate_text_report(results, output_path="relatorio_icoer.txt"):
    with open(output_path, 'w', encoding='utf-8') as f:
        for k, v in results.items():
            f.write(f"{k}: {v}\n")

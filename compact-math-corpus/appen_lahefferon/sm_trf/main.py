from trf_stats_summary import generate_trf_summary
from trf_detailed_stats import generate_trf_detailed

def main():
    json_input = "data/pdfappen-lahefferon.json"  # Replace with your JSON file
    summary_output = "outputs/trfappen-stats-summary.csv"
    detailed_output = "outputs/trfappen-lahefferon-stats.json"

    print("Generating summary statistics with Transformer model...")
    generate_trf_summary(json_input, summary_output)

    print("Generating detailed statistics with Transformer model...")
    generate_trf_detailed(json_input, detailed_output)

if __name__ == "__main__":
    main()


from fpdf import FPDF

class CombinedPDFReport(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, "Comprehensive Client Report", ln=True, align="C")

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", 0, 0, "C")

    def add_behavior_section(self, profile, score, recommendations, responses):
        self.add_page()
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Behavioral Profile Summary", ln=True)
        self.set_font("Arial", "", 12)
        self.cell(0, 10, f"Behavioral Profile: {profile}", ln=True)
        self.cell(0, 10, f"Behavioral Score: {score}", ln=True)

        self.ln(5)
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Responses:", ln=True)
        self.set_font("Arial", "", 11)
        for i, (question, answer) in enumerate(responses):
            self.multi_cell(0, 10, f"{i+1}. {question}\n   Answer: {answer}")
            self.ln(1)

        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Recommendations:", ln=True)
        self.set_font("Arial", "", 11)
        for rec in recommendations:
            self.multi_cell(0, 10, f"- {rec}")
        self.ln(10)

    def add_portfolio_section(self, summary, uploaded_df):
        self.add_page()
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Uploaded Portfolio", ln=True)
        self.set_font("Arial", "", 10)
        for idx, row in uploaded_df.iterrows():
            self.cell(0, 10, f"{row['Ticker']}: {row['Weight (%)']}%", ln=True)

        self.ln(5)
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Portfolio AI Analysis", ln=True)
        self.set_font("Arial", "", 10)
        self.cell(0, 10, f"Total Holdings: {summary['Total Holdings']}", ln=True)
        self.cell(0, 10, f"Total Weight: {summary['Total Weight']}%", ln=True)

        self.ln(4)
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Overweight Holdings", ln=True)
        self.set_font("Arial", "", 10)
        if summary["Overweight Assets"]:
            for ticker, delta in summary["Overweight Assets"]:
                self.cell(0, 10, f"{ticker}: Overweight by {delta}%", ln=True)
        else:
            self.cell(0, 10, "None", ln=True)

        self.ln(3)
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Underweight Holdings", ln=True)
        self.set_font("Arial", "", 10)
        if summary["Underweight Assets"]:
            for ticker, delta in summary["Underweight Assets"]:
                self.cell(0, 10, f"{ticker}: Underweight by {delta}%", ln=True)
        else:
            self.cell(0, 10, "None", ln=True)

        self.ln(3)
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Missing From Model", ln=True)
        self.set_font("Arial", "", 10)
        if summary["Missing from Model"]:
            for ticker in summary["Missing from Model"]:
                self.cell(0, 10, f"{ticker}", ln=True)
        else:
            self.cell(0, 10, "None", ln=True)

        self.ln(3)
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Suggested Allocation", ln=True)
        self.set_font("Arial", "", 10)
        for ticker, weight in summary["Suggested Allocation"].items():
            self.cell(0, 10, f"{ticker}: {weight}%", ln=True)

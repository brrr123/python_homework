import pandas as pd

class DFPlus(pd.DataFrame):
    @property
    def _constructor(self):
        return DFPlus

    @classmethod
    def from_csv(cls, filepath, **kwargs):
        df = pd.read_csv(filepath, **kwargs)
        return cls(df)
    
    def print_with_headers(self):
        total_rows = len(self)

        for i in range(0, total_rows, 10):
            end_idx = min(i + 10, total_rows)
            chunk = super().iloc[i:end_idx]

            print(chunk.to_string())

            if end_idx < total_rows:
                print("\n" + "-" * 40 + "\n")


if __name__ == "__main__":
    dfp = DFPlus.from_csv("../csv/products.csv")

    print("Printing DataFrame with headers every 10 rows:")
    dfp.print_with_headers()
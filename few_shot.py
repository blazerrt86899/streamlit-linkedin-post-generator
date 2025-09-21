import json
import pandas as pd

class FewShotsPost:
    def __init__(self, file_path="./data/processed_posts.json"):
        self.df = None
        self.unique_tags = None
        self.load_posts(file_path=file_path)
        
    def load_posts(self, file_path):
        with open(file=file_path, encoding='utf-8') as file:
            self.df = pd.json_normalize(json.load(file))
            self.df["length"] = self.df["line_count"].apply(self.categorize_length)
            all_tags = self.df["tags"].apply(lambda x: x).sum()
            self.unique_tags = set(list(all_tags))
    
    def categorize_length(self, line_count):
        if line_count < 10:
            return "Short"
        elif 10 <= line_count <= 15:
            return "Medium"
        else:
            return "Long"
      
    def get_tags(self):
        return self.unique_tags
    
    def get_unique_creators(self):
        all_creators = [ creator for creator in self.df["creator"] ]
        unique_creators = list(set(all_creators))
        return unique_creators
    
    def get_filtered_posts(self, length, language, tag, creator):
        df_filtered = self.df[
            (self.df["language"] == language) &
            (self.df["length"] == length) &
            (self.df["tags"].apply(lambda tags: tag in tags)) &
            (self.df["creator"] == creator)
        ]
        return df_filtered.to_dict(orient="records")

if __name__ == "__main__":
    fs = FewShotsPost()
    posts = fs.get_filtered_posts("Short", "Hinglish", "Artificial Intelligence","Romu")
    print(posts)
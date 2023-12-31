from dataset.download_data import download_amazon_review_data
from dataset.data_preprocessor import preprocess
from train import train_model, NCFDataset
from torch.utils.data import DataLoader
from models.NeuralCF import NCF

#modify the ratings name variable to change dataset
ratings_name = "ratings_Home_and_Kitchen"
downloaded_data = download_amazon_review_data(ratings_name)
print(downloaded_data)
processed_train, processed_test, num_users, num_items  = preprocess(ratings_name)

train_dataset = NCFDataset(processed_train)
train_loader = DataLoader(train_dataset, batch_size=4096, shuffle=True)

# Hyperparameters
num_factors = 50
nums_hiddens = [128, 64, 32, 16, 8]

# Create model instance
ncf = NCF(num_factors, num_users, num_items, nums_hiddens)

# Train the model
train_model(ncf, train_loader, processed_test, num_users, num_items, top_k=10, user_sample_ratio=0.2, num_epochs=10, learning_rate=0.01)

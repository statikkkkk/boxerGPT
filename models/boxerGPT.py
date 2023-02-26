import pytorch_lightning as pl
from models.model import GPT
import torch


class boxerGPT(pl.LightningModule):
    def __init__(self, gptconf):
        super().__init__()
        self.gptconf = gptconf
        self.model = GPT(gptconf)
        self.forward = self.model.forward
        self.generate = self.model.generate
        
    def training_step(self, batch, batch_idx):
        # training_step defines the train loop.
        # it is independent of forward
        x, y = batch
        logits, loss = self.model.forward(x, targets=y)
        # Logging to TensorBoard (if installed) by default
        self.log("train_loss", loss)
        return loss
    
    @torch.no_grad()
    def validation_step(self, batch, batch_idx):
        # training_step defines the train loop.
        # it is independent of forward
        x, y = batch
        logits, loss = self.model.forward(x, targets=y)
        # Logging to TensorBoard (if installed) by default
        self.log("val_loss", loss)

    def configure_optimizers(self):
        return self.model.configure_optimizers(
            weight_decay=self.gptconf.weight_decay,
            learning_rate=self.gptconf.learning_rate,
            betas=self.gptconf.betas,
            device_type=self.gptconf.device_type,
        )

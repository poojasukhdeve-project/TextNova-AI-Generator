# train a miniature character-level shakespeare model
# good for debugging and playing on macbooks and such

out_dir = 'out-movies'
eval_interval = 200 # keep frequent because we'll overfit
eval_iters = 100
log_interval = 20 # don't print too too often

# we expect to overfit on this small dataset, so only save when val improves
always_save_checkpoint = True

wandb_log = False # override via command line if you like
wandb_project = 'movies-gpt'
wandb_run_name = 'mini-gpt'

dataset = 'movies' # the only option for now, but you could add your own datasets in data/
gradient_accumulation_steps = 1
batch_size = 64
block_size = 256 # context of up to 256 previous characters

# baby GPT model :)
n_layer = 6
n_head = 4
n_embd = 192
dropout = 0.1

learning_rate = 3e-4 # with baby networks can afford to go a bit higher
max_iters = 8000
lr_decay_iters = 8000 # make equal to max_iters usually
min_lr = 3e-5 # learning_rate / 10 usually
beta2 = 0.99 # make a bit bigger because number of tokens per iter is small

warmup_iters = 200 # not super necessary potentially

device = 'cpu'      # ✅ ADD THIS
compile = False     # ✅ ADD THIS

# on macbook also add
# device = 'cpu'  # run on cpu only
# compile = False # do not torch compile the model

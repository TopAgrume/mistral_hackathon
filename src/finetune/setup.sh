# Modify 7B.yaml with your training and test files, and set hyperparameters

# IN mistral-finetune folder :

python3 -m utils.validate_data --train_yaml 7B.yaml

export CUDA_VISIBLE_DEVICES=0
torchrun --nproc-per-node 1 --master_port $RANDOM -m train 7B.yaml

mistral-chat ./mistral_models/7B_instruct --max_tokens 4096 --temperature 1.0 --instruct --lora_path {run_dir FROM .yaml config}/checkpoints/checkpoint_000300/consolidated/lora.safetensors

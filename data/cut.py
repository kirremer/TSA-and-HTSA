import numpy as np

# 分割大文件
def split_npy(filepath, max_size_mb=95):
    # 加载原始数组
    data = np.load(filepath)
    
    # 计算每个分片的大小（字节）
    max_size_bytes = max_size_mb * 1024 * 1024
    total_bytes = data.nbytes
    
    # 基于数组第一维度分割
    items_per_file = max(1, int((max_size_bytes / total_bytes) * len(data)))
    
    # 分割并保存
    num_files = int(np.ceil(len(data) / items_per_file))
    base_name = filepath.replace('.npy', '')
    
    for i in range(num_files):
        start_idx = i * items_per_file
        end_idx = min((i + 1) * items_per_file, len(data))
        chunk = data[start_idx:end_idx]
        output_file = f"{base_name}_part{i+1}.npy"
        np.save(output_file, chunk)
        print(f"保存分片 {i+1}/{num_files}: {output_file}")
    
    # 创建合并指南文件
    with open(f"{base_name}_merge_guide.txt", "w") as f:
        f.write(f"原始文件: {filepath}\n")
        f.write(f"分片数量: {num_files}\n")
        f.write("合并代码示例:\n\n")
        f.write("```python\n")
        f.write("import numpy as np\n\n")
        f.write(f"parts = []\n")
        for i in range(num_files):
            f.write(f"parts.append(np.load('{base_name}_part{i+1}.npy'))\n")
        f.write(f"merged = np.concatenate(parts)\n")
        f.write(f"np.save('{filepath}', merged)  # 恢复原始文件\n")
        f.write("```\n")

# 使用示例
split_npy('./HTSA/X_htsa.npy')
split_npy('./TSA/X_tsa.npy')
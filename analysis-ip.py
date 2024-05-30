import re
from collections import defaultdict

def find_ips_in_file(file_path):
    # 使用正则表达式匹配IP地址
    ip_regex = re.compile(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b')
    ips_found = []

    with open(file_path, 'r') as file:
        for line in file:
            ips_found.extend(ip_regex.findall(line))

    return ips_found

def group_ips_by_c_segment(ips):
    # 按C段分组IP地址
    c_segment_ips = defaultdict(list)

    for ip in ips:
        # 生成C段的唯一标识，例如：192.168.1
        c_segment_prefix = '.'.join(ip.split('.')[:-1])
        c_segment_ips[c_segment_prefix].append(ip)

    return c_segment_ips

def write_results_to_file(c_segments_ips, output_file):
    # 将结果写入文件中
    with open(output_file, 'w') as file:
        for c_segment, ips in c_segments_ips.items():
            if len(ips) > 1:  # 过滤掉只有一个IP地址的C段
                file.write(f"{c_segment}: {len(ips)} IPs\n")
                for ip in ips:
                    file.write(f"  - {ip}\n")
                file.write("-" * 20 + "\n")  # 分隔线

if __name__ == "__main__":
    input_file_path = 'ip.txt'  # 替换为你的文件路径
    output_file_path = 'C-ip.txt'  # 输出文件的名称
    ips_found = find_ips_in_file(input_file_path)
    c_segments_ips = group_ips_by_c_segment(ips_found)
    write_results_to_file(c_segments_ips, output_file_path)

    print(f"结果已被写入到文件 {output_file_path}。")
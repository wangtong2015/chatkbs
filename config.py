import os
import argparse

parser = argparse.ArgumentParser(description='Description of your program')

parser.add_argument('-p', '--port', help='端口，默认是10001', default=10001)
parser.add_argument('--cuda', help='cuda序号，-1表示不使用cuda，默认是0', default=0)
parser.add_argument('--name', help='用户登录名称，默认是chatkbs', default='chatkbs')
parser.add_argument('--password', help='用户登录密码，默认是chatkbs', default='chatkbs')
parser.add_argument('--share', action='store_true', help='是否用Gradio共享链接')

args = parser.parse_args()

VERSION_NAME = '1.0.3'
VERSION_CODE = 4

# 获取当前工作目录的绝对路径
BASE_DIR = os.getcwd()

USERNAME = args.name
PASSWORD = args.password

SERVER_PORT = args.port
SERVER_NAME = '0.0.0.0'
FAVICON = 'favicon.png'
SHARE = args.share

CUDA = args.cuda
DATA_DIR = 'data'

SQLITE_DATABASE = f'database-{VERSION_NAME}.db'

CHATGLM_MODEL_PATH = 'THUDM/chatglm-6b'

MILVUS_COLLECTION_KBS_CHUNK = f'kbs_chunk_{VERSION_CODE}'
MILVUS_COLLECTION_KBS_FILE = f'kbs_file_{VERSION_CODE}'

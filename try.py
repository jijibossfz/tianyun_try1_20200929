# coding=utf-8
import io

from PIL import Image
from rdkit import Chem
from rdkit.Chem import Draw

smi = '[Na+].[O-][Cl+3]([O-])([O-])[O-]'
m = Chem.MolFromSmiles(smi)
print(m)
Draw.MolToImageFile(m, 'mol.jpg')

import base64
from io import BytesIO

# img_buffer = BytesIO()
# a.save(img_buffer, format='JPEG')
# byte_data = img_buffer.getvalue()
# base64_str = base64.b64encode(byte_data)
# print(base64_str)
# 图片转字节
# with open('mol.jpg', 'rb') as fp:
#     tu = base64.b64encode(fp.read())
#     print(tu)
# m = Chem.MolFromMol2File('/home/wz/pywork/try27/drug/media/dock/961445782@qq.com/1200/1_X77_orig.mol2')
# Draw.MolToImageFile(m, 'molx.jpg')

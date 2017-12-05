import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np



# red_patch = mpatches.Patch(color='red', label='Pyr_2')
# green_patch = mpatches.Patch(color='green', label='Pyr_1')
# blue_patch = mpatches.Patch(color='blue', label='Phen')
# black_patch = mpatches.Patch(color='black', label='TBP')
#
# plt.legend(handles = [red_patch, green_patch, blue_patch, black_patch])
# LanList = ["La", "Eu", "Lu"]
# plt.xticks([1, 2, 3], LanList)
plt.plot([0.1145, 0.1152, 0.143867, 0.170845, 0.153635, 0.139935, 0.111661, 0.139931],
         [-0.105102998, -0.097385645, -0.13597241, -0.16537185, -0.147364693, -0.137442382, -0.10289804, -0.113187844], 'ro')
plt.ylabel('Energy_Gap, DFT, (Eh)')
plt.xlabel('Energy_Gap, TD_DFT, (Eh)')
i = 1
for a,b in zip([0.1145, 0.1152, 0.143867, 0.170845, 0.153635, 0.139935, 0.111661, 0.139931],
               [-0.105102998, -0.097385645, -0.13597241, -0.16537185, -0.147364693, -0.137442382, -0.10289804, -0.113187844]):
    plt.text(a, b, i)
    i = i + 1

plt.show()
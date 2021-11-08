# MassiveSumm: a very large-scale, very multilingual, news summarisation dataset
This repository contains links to data and code to fetch and reproduce the data described in our EMNLP 2021 paper titled "[MassiveSumm: a very large-scale, very multilingual, news summarisation dataset](https://aclanthology.org/2021.emnlp-main.797/)". A (massive) multilingual dataset consisting of 92 diverse languages, across 35 writing scripts. With this work we attempt to take the first steps towards providing a diverse data foundation for in summarisation in many languages.

> *Disclaimer: The data is noisy and recall-oriented. In fact, we highly recommend reading  our analysis on the efficacy of this type of methods for data collection.*


## Get the Data
Redistributing data from web is a tricky matter. We are working on providing efficient access to the entire dataset, as well as expanding it even further. For the time being we only provide links to reproduce subsets of the entire dataset through either common crawl and the wayback machine. The dataset is also available upon request ([djam@itu.dk](mailto:djam@itu.dk)).


In the table below is a listing of files containing URLs and metadata required to fetch data from common crawl.
lang  |  wayback                                                                         |  cc
------|----------------------------------------------------------------------------------|--------------------------------------------------------------------------------
afr   |  [link](https://drive.google.com/file/d/1m7ctoWs5or8HsFbuW5pBu_PodpND0J3e/view)  |  -
amh   |  [link](https://drive.google.com/file/d/1k0_65Zb00VGm5i-hnFYuY7lNzjVUiWvl/view)  |  [link](https://drive.google.com/file/d/1_awz_-B0iWtaPdKih8H8Kz4HGnJSwvRq/view)
ara   |  [link](https://drive.google.com/file/d/1raYOtsrpmD-yAGo50Kr917Ns3tXEJBci/view)  |  [link](https://drive.google.com/file/d/1HvCeJ3p59sdhb1xLFGNVHr10hHEg8phA/view)
asm   |  [link](https://drive.google.com/file/d/1iGPZdk-PKQn0M_q8ENl-sJY861sT0kaE/view)  |  -
aym   |  [link](https://drive.google.com/file/d/12XzyUHfrOi317OLU0QsOgl6eZvVOK-bF/view)  |  -
aze   |  [link](https://drive.google.com/file/d/1JIqaeoNJt3VATqqjzP27fUBlTAlCvagz/view)  |  [link](https://drive.google.com/file/d/1CftuzziqiR5QezH9oYL-bCE_KpKdKQgK/view)
bam   |  [link](https://drive.google.com/file/d/1Yb9YOENj0Kf8FK19eXHD-iHu5nuqR_3-/view)  |  [link](https://drive.google.com/file/d/1MWQVJMBLmc_8qktep7FGohVbHdXR0iKx/view)
ben   |  [link](https://drive.google.com/file/d/1lOso52ouqtddUGF5RGOkIlVfL3kD3oTB/view)  |  [link](https://drive.google.com/file/d/1wK6YTRkXuc4df8C-Ko-PaWB1pIeDfY8q/view)
bod   |  [link](https://drive.google.com/file/d/1RmonaYMfzj-sw5uM1crJvJxn1FEWfDNi/view)  |  [link](https://drive.google.com/file/d/1vnZb9PUjRCX6E__OlCAqBGxdu3-19Q8W/view)
bos   |  [link](https://drive.google.com/file/d/1alV_CwZpxzAcEfuBCp5TCeMr3qOPZZHW/view)  |  [link](https://drive.google.com/file/d/1TTQVPZ4G7TGy7mFnN21XC3ZDlJlTpGhM/view)
bul   |  [link](https://drive.google.com/file/d/1XU56P9Jd4Meo7YCEedRPu3qd3nOZRvSx/view)  |  [link](https://drive.google.com/file/d/13MJzUdrCLz-lo_c4IZOOupJY_50zvZHd/view)
cat   |  [link](https://drive.google.com/file/d/1OqPLjlsUI-ldg6z2eEe_hA1tM1MCAfEt/view)  |  -
ces   |  [link](https://drive.google.com/file/d/1na5Wx9P4SyVfHgIhRhFJ8RH0WpP2qAwt/view)  |  [link](https://drive.google.com/file/d/1tKzsoGFdDo93aKfEpkY5sSLsuN1hL4LV/view)
cym   |  [link](https://drive.google.com/file/d/1wqb_fsyw9GBouoHkGq353nWXJZLAL4Ax/view)  |  [link](https://drive.google.com/file/d/1ewLaDdoC1An4hYr6LVLnPGPsY5h0ZiqS/view)
dan   |  [link](https://drive.google.com/file/d/10Isyjz0Lw9F2JU3Lw4msLma49_i3CVJo/view)  |  [link](https://drive.google.com/file/d/1-VcQxG_YDngEaNNRBMn9vl6L3sIEnL_8/view)
deu   |  [link](https://drive.google.com/file/d/1dguGPFKXkTvSVn2Yuyv7kBqWROouo7nM/view)  |  [link](https://drive.google.com/file/d/1LfBPlYTbmjWnZTM_e6twUVgzrOjY2kfp/view)
ell   |  [link](https://drive.google.com/file/d/1hyQJHMMTP0WPaEMPeK5WpoToGuMU1m1C/view)  |  [link](https://drive.google.com/file/d/1dzbQc2K_rTIrkpcw9UgQyZ4PPk_ZYF5i/view)
eng   |  [link](https://drive.google.com/file/d/1WumR27bj54A_ObzbM1FX7aR0Xiv80g8n/view)  |  [link](https://drive.google.com/file/d/1u-Zt56FKrJ9zVZRRSPiwqIoGaKHkTOuY/view)
epo   |  [link](https://drive.google.com/file/d/1akp7L7cE9J75hdmxkjXIhLO30c1uZzV3/view)  |  -
fas   |  [link](https://drive.google.com/file/d/1feVopBcYgz6TybgpYJjNma8Q8v1V36nT/view)  |  [link](https://drive.google.com/file/d/1AMz5xhJaR9Ud-oic4LA4-VoBfcT-cqWH/view)
fil   |  [link](https://drive.google.com/file/d/16PBhI9DJZxju2du56u3OTgga-L7ImdKY/view)  |  -
fra   |  [link](https://drive.google.com/file/d/19PCGH6Hxt2YiIiEcP224qSQ94D2f49lc/view)  |  [link](https://drive.google.com/file/d/1UQitwbOPwbbaXFb8xtV0chjeLvWzm3LN/view)
ful   |  [link](https://drive.google.com/file/d/1glT_e_2kO9bb3mTRCYWUs4n0zGFBS8q9/view)  |  [link](https://drive.google.com/file/d/1eku0kULX4ZE9wQnUJMcqHy65Jsu21FFp/view)
gle   |  [link](https://drive.google.com/file/d/1o078h9dEo2bJdmSmex2NA31yt491Cx_X/view)  |  [link](https://drive.google.com/file/d/1HNVxzYdmc1l_q4UOwNV6Yh2_QMfmlSaf/view)
guj   |  [link](https://drive.google.com/file/d/19s9xs6DPeplFv3ME3V1Lhk7Zr_YJ3SMD/view)  |  [link](https://drive.google.com/file/d/1PWFIVGeCRuzAHH-w2UwVOANSvyeEXgFk/view)
hat   |  [link](https://drive.google.com/file/d/1ioS9mTDjMlNOl8Z7by9F_YIT4BwZnEn-/view)  |  [link](https://drive.google.com/file/d/1yDorOERjCNFdDRt9viZyWpcO7gmXDyvr/view)
hau   |  [link](https://drive.google.com/file/d/1oSLe6bPcfqkOtarZ5f5l_jBFLO2_Tafb/view)  |  [link](https://drive.google.com/file/d/1cYkwEYclvHnN8BLZf6z-DEyINGAHy34L/view)
heb   |  [link](https://drive.google.com/file/d/1tHlRd6bg5zS7xvaEp5JOST7Ngb-DHecX/view)  |  -
hin   |  [link](https://drive.google.com/file/d/1RDbFOOMV3FC71R_1QKxocwDgxP8csmqz/view)  |  [link](https://drive.google.com/file/d/1ZNcCqUV15Bv2FlY3qkMYyBWBm0hO4LKI/view)
hrv   |  [link](https://drive.google.com/file/d/13PlLYJmEbZAc8mgMHbZH58-rLvU8bLSY/view)  |  -
hun   |  [link](https://drive.google.com/file/d/157CC5cPhpWg5aM4iMjNtX0CdVyL1yO-J/view)  |  [link](https://drive.google.com/file/d/1R52kqwahdPHFkGpsGdAJE6Wkq38UGgFS/view)
hye   |  [link](https://drive.google.com/file/d/1ZX0FmoSAmC_QJdwNo-KlqjrLG8ALup5L/view)  |  [link](https://drive.google.com/file/d/1ciACol27dN07_omNInoU_NqUvYmwXo6C/view)
ibo   |  [link](https://drive.google.com/file/d/11cmywemBJuNeHkdwn_a4rPyKqbOM7zYF/view)  |  [link](https://drive.google.com/file/d/1oYOHwATB0PWNYvEv-azy_8MUgkxzFZCY/view)
ind   |  [link](https://drive.google.com/file/d/1Cb0sJ-2cLYQdg3hKG7yC4bCziYjtpFRo/view)  |  [link](https://drive.google.com/file/d/1Sch920J5PqJbhpEQHNTjJ1ojiMU46tiQ/view)
isl   |  [link](https://drive.google.com/file/d/183aUjkvgPtyafmAh3fvUj1OjFloa-nC6/view)  |  [link](https://drive.google.com/file/d/1wzccfq0RAN7c5c2BGhNMySp2yMYfj9ep/view)
ita   |  [link](https://drive.google.com/file/d/1eGrviIr8FiRPaIK51l9mFbKEpr_RryuN/view)  |  [link](https://drive.google.com/file/d/123eRVzORxPIQnp75RMf0LsXWL21l76IH/view)
jpn   |  [link](https://drive.google.com/file/d/16wRlWIwPIl3tBLJbrWRxDbnehLHHOWEt/view)  |  [link](https://drive.google.com/file/d/1vjYBbEmWg8PoztrcSqDjUe7ClCUNKHAL/view)
kan   |  [link](https://drive.google.com/file/d/1J7jD8MjKkR0c_7OIZ7ahw4Bq_2jTgrYX/view)  |  [link](https://drive.google.com/file/d/18rBERL7l4zBupWwVHXasPu3jlegCM31B/view)
kat   |  [link](https://drive.google.com/file/d/1S-CYer6Yu02tMRLBbxHtKFYCp33gXBzc/view)  |  [link](https://drive.google.com/file/d/1GSpqPf87onRlKHu4yoLzxQkAOSIE1GVW/view)
khm   |  [link](https://drive.google.com/file/d/11OL9JKSTT8_zVQl77avrEVQiqXqV1J2p/view)  |  [link](https://drive.google.com/file/d/1-0m54dcSjGyBST9bodw1RJYqICsZCwuS/view)
kin   |  [link](https://drive.google.com/file/d/1DnRV2pUU-b-f9DT27AtNLRJcx31AuRy4/view)  |  -
kir   |  [link](https://drive.google.com/file/d/1DoBBN_nb_V-Ogl94KL-nM6iJH2WaGOpK/view)  |  [link](https://drive.google.com/file/d/1ncixaRUVSGcgTrMPhibN1Pfd4yIJ8c15/view)
kor   |  [link](https://drive.google.com/file/d/1L3RY0coCdd-1HX4r0VkU2kQYdFOMuN_9/view)  |  [link](https://drive.google.com/file/d/14-QZft00ab2KAtjT1-p1fvaA45qKt3JJ/view)
kur   |  [link](https://drive.google.com/file/d/15a_TBIEC1jYNVOTh_wKpKUrW8w_p3FoW/view)  |  [link](https://drive.google.com/file/d/1g3WTVRxMo5M5HOBuNJLU7KdSw1RQRdTx/view)
lao   |  [link](https://drive.google.com/file/d/1oO7L92P1XUD6cNdh5MlDv9R-6jLjaYix/view)  |  [link](https://drive.google.com/file/d/1IOcXBGMoaA859RXzrXSV1WS2qMOweRUn/view)
lav   |  [link](https://drive.google.com/file/d/1K6Z0RLc0yvyqHXIy3wYh8Elr3QlIMltz/view)  |  [link](https://drive.google.com/file/d/1AdXmbWraGH_Dh9_f2CcQhhqP5hIqnJXu/view)
lin   |  [link](https://drive.google.com/file/d/1JTgwLaQgMSqOvdARhw82zrCwZpv5OFZV/view)  |  [link](https://drive.google.com/file/d/1QDYxfhMQDZeGVVRUsZjUzf7C2RUMYDMR/view)
lit   |  [link](https://drive.google.com/file/d/1df6oV_UxxqZQnYRtmkVxUZe-2b4Bsiay/view)  |  [link](https://drive.google.com/file/d/1WjIJ-LZN0ZdqtE_NnoEiAiNhXm3eRGHk/view)
mal   |  [link](https://drive.google.com/file/d/1hqp4OmL27HPBMVhYwZLf28Syha7mDmqx/view)  |  [link](https://drive.google.com/file/d/1tvsdnjRAiBFHc0Py-duJoqPlSwYlokie/view)
mar   |  [link](https://drive.google.com/file/d/1BRcMJL_Zk1rq0hNcCYZAbZ3nMF0qmM1I/view)  |  [link](https://drive.google.com/file/d/1Z-ui3IipNQy3jpQqeNzrQiVZcXnUFs2e/view)
mkd   |  [link](https://drive.google.com/file/d/1-UzcYkog_TjAnk9DjTR6vN29R3qjHICN/view)  |  [link](https://drive.google.com/file/d/1xpE3nPcs-m5WdbPyOX1H4wt9k06NMKN3/view)
mlg   |  [link](https://drive.google.com/file/d/1dhzWeA8-JKFbhoLpbV1Yli5M4XHkrXdu/view)  |  [link](https://drive.google.com/file/d/11mpExgMv7VSdejMXUQLFnnPwitLUNudw/view)
mon   |  [link](https://drive.google.com/file/d/1bPHLSMKtCI927f-I_skf0T98HAp-jN-A/view)  |  [link](https://drive.google.com/file/d/1rejguZ0HNNMZdV_9g6qXT6Si6QVXhuge/view)
mya   |  [link](https://drive.google.com/file/d/1fXyMEKX8sz8-wCOKoLLXuqLXMsFZs9Ld/view)  |  [link](https://drive.google.com/file/d/1cLre9C9f1lm2Ds_8hv6f7h2R4phrXtVd/view)
nde   |  [link](https://drive.google.com/file/d/1b_UekJ498qQv2DzeXjUWL20VMftds0ec/view)  |  [link](https://drive.google.com/file/d/1KxB5RLGMlteQOqBYu2DOhIXVzCUkhvDM/view)
nep   |  [link](https://drive.google.com/file/d/1g-tRWW1dweVZMtkWnkm4j5-Qnbwzlh2P/view)  |  [link](https://drive.google.com/file/d/1jw_P1wenbskDfG8iQD3dYRb0oWnRba9N/view)
nld   |  [link](https://drive.google.com/file/d/1JwV508z5Bx_3dHjCW0lMAhp0-8ykF7sF/view)  |  -
ori   |  [link](https://drive.google.com/file/d/1eWnnCigfd8HmMueSvyPe7x1JcvGFReg2/view)  |  [link](https://drive.google.com/file/d/1a3t0X7PfphDZJiyJSL-FzsoZsDH9KIu4/view)
orm   |  [link](https://drive.google.com/file/d/1oZ4S71rijKd32IL9Ww8VR-vr1mzh4WVT/view)  |  [link](https://drive.google.com/file/d/1-SopeFs8niXlmwWSe117-YDQ6ECK8xTh/view)
pan   |  [link](https://drive.google.com/file/d/1Yr6Cy_gaJrbWNHz5khkjDR4mKZT7_TMO/view)  |  [link](https://drive.google.com/file/d/1t3sUOR_m4blOj8iIU1q8ohxUWPTWImcw/view)
pol   |  [link](https://drive.google.com/file/d/1BSX_LcGIaDQOWXDqC3YmMFmRM2DQbUYb/view)  |  [link](https://drive.google.com/file/d/1pNOSculzyCNMjrQOarVhG_SDg1IbMpBr/view)
por   |  [link](https://drive.google.com/file/d/1KWnsUKgIb2fJlRcOq0WhCzyE8cR0LhfB/view)  |  [link](https://drive.google.com/file/d/13ET2tIsrzFTzlb9Rd2KAp-FF7Y6R2Ker/view)
prs   |  [link](https://drive.google.com/file/d/1izhl77L8R2r7YM4-Usu0VMAQtoO5sn7R/view)  |  [link](https://drive.google.com/file/d/11QMxXjH9vN0V6-UZXT2omxb7lm8zphqC/view)
pus   |  [link](https://drive.google.com/file/d/1nJ0hBzj0z51htnwftGyd_I0DQbFdeypS/view)  |  [link](https://drive.google.com/file/d/1nccq6pEsvUhe1zvPTDoDKEob6cRKPpWP/view)
ron   |  [link](https://drive.google.com/file/d/1XxDdroLJdAQZwtGmhPedZ-YZq_G9T-tr/view)  |  -
run   |  [link](https://drive.google.com/file/d/1FVLjZI_oj6bGwP6tIMUTY-8yj4pjJm-5/view)  |  [link](https://drive.google.com/file/d/165N8Wh_TeTo7N_el6eWGmZ5ts3KBKU9Q/view)
rus   |  [link](https://drive.google.com/file/d/17RWgFR6mIvxGr6RGhuRZspLtnlWZk1Ul/view)  |  [link](https://drive.google.com/file/d/15Cqcrbl_lG_oSED_hTyR_mb-dwpvw9J8/view)
sin   |  [link](https://drive.google.com/file/d/158EtvATjJ39G7vThM69h4shcRqRXdT9K/view)  |  [link](https://drive.google.com/file/d/1gvqSIOkL7RDX-yg7O1VwHTdRUcNGcf_F/view)
slk   |  [link](https://drive.google.com/file/d/1IGtxqiLlJqBhsfgbAUlyQAwQir2QmYGb/view)  |  [link](https://drive.google.com/file/d/1GDzuxd-KhBA_fHrDlO8HcCayLsG4-UkX/view)
slv   |  [link](https://drive.google.com/file/d/1gWb-pImthObUPJ16hIO5HZif3XSvjIrK/view)  |  [link](https://drive.google.com/file/d/1T71uVRLX-wB-qeWFMyqtxlI91Dr2u7pn/view)
sna   |  [link](https://drive.google.com/file/d/1FOacYT0S5sPVxmBbH4mHsH4uyrbQwOoM/view)  |  [link](https://drive.google.com/file/d/1wCysDOCUvsA3H-9CmrItwU7GHIxQt1rU/view)
som   |  [link](https://drive.google.com/file/d/1IHxrknewcaTTQKrCH6K00lz3dPT5lIUc/view)  |  [link](https://drive.google.com/file/d/1oXDsB76ViX9ri5W_2xVEQqLWDqIQAh5O/view)
spa   |  [link](https://drive.google.com/file/d/1y3iDoCDfT19MXgQtQ_z_dF4q8xgLK4Eq/view)  |  [link](https://drive.google.com/file/d/14dX8cePpcb-E7nS8brupu9lQkoLUPLSf/view)
sqi   |  [link](https://drive.google.com/file/d/1rpOjaE3mjyl8LsLcU5QiEt1xmkxF0ntW/view)  |  [link](https://drive.google.com/file/d/1jz5sXn8JeHhZHjXb7r0wLqyynva7c8Al/view)
srp   |  [link](https://drive.google.com/file/d/1wpp_f10LNB4Qb0F8-EMmdKWLMHb4cGuw/view)  |  [link](https://drive.google.com/file/d/1XJCyan1OL3UTI9_tNbvZX2ngQ2bhoy0U/view)
swa   |  [link](https://drive.google.com/file/d/1L3DHVdngIRSd8eCjx7qyp5NBwziz6I6B/view)  |  [link](https://drive.google.com/file/d/1ukbOFz_dHYaIQnD4ub0hE9DqF_1mwVke/view)
swe   |  [link](https://drive.google.com/file/d/1BgVrlj40Mlg4yOOMy1yPV8iyFbZTrRLE/view)  |  -
tam   |  [link](https://drive.google.com/file/d/1VrmX5egg4zaZKPBA0Ic3jlMg_ovYkeW9/view)  |  [link](https://drive.google.com/file/d/1DWv-hkU0P2B0AysTFwOZ3aghW6lxF16A/view)
tel   |  [link](https://drive.google.com/file/d/1zo3gNIH2sMczXpnWh-vVty3pr4-tOaBy/view)  |  [link](https://drive.google.com/file/d/1e0KIPqcKYHXmSjgLpxLJkEFumw8Bae_g/view)
tet   |  [link](https://drive.google.com/file/d/1n-PVdlyti6wGtlGUalYeHOmGwZtG6xDe/view)  |  -
tgk   |  [link](https://drive.google.com/file/d/1g6_1YKJbv7-5glBsreqspPP_VnBsRSXW/view)  |  -
tha   |  [link](https://drive.google.com/file/d/1vTBPYxmkyWCqnboX3cVxxNHcfRcXAo_7/view)  |  [link](https://drive.google.com/file/d/197vyuI2JzOGczeVRqnUGu78G3T2WWRit/view)
tir   |  [link](https://drive.google.com/file/d/1vkt2SRGiSPIJKzgU-XagWmx6rnQLtmZZ/view)  |  [link](https://drive.google.com/file/d/1lDazmqixV4Gem96O-c-gulqSNKUEcjnR/view)
tur   |  [link](https://drive.google.com/file/d/1_39Hk7K-IKzvSiRLmue1mxANuPXQg9p5/view)  |  [link](https://drive.google.com/file/d/1Kole41CnnNArIt_rxfNlimk9EMQZFa8Y/view)
ukr   |  [link](https://drive.google.com/file/d/1h2I-yan3WcVEyJfeyJD_fFFviJWK93N3/view)  |  [link](https://drive.google.com/file/d/1H8TUR73sJs_bvjJuLNB4szqiCIvTq5sp/view)
urd   |  [link](https://drive.google.com/file/d/1p-lG1vEDp838GRzuPWc9hjfZeqjfeMh3/view)  |  [link](https://drive.google.com/file/d/1HDwEMuaULkZr6Mm39CifS2szyI_vql-G/view)
uzb   |  [link](https://drive.google.com/file/d/134swKYwYcfCFbMSXe16hvmLVGqS7pOMb/view)  |  [link](https://drive.google.com/file/d/1nYOLG5UlV-YDeex8Tvi37hK4pM9wD7Wg/view)
vie   |  [link](https://drive.google.com/file/d/1zm1AjKpOhEeaZgs2MeJsrFVjxT7kbyFL/view)  |  [link](https://drive.google.com/file/d/1uts1nSGwWNxEFZnsJi6SdamG2DAVPq-q/view)
xho   |  [link](https://drive.google.com/file/d/1Gkq4cLknzh_cY9HBlWAGqkZez31vIarY/view)  |  [link](https://drive.google.com/file/d/1P31PeL7cVJ9eNE-YZ0ofH0pozT9ta5bP/view)
yor   |  [link](https://drive.google.com/file/d/1KhCZk7wBsFkKsmU4XWffVTS37w1FguwE/view)  |  [link](https://drive.google.com/file/d/17ifvygtGzaIgDuqiFK0QDK1Jd7SOnkNd/view)
yue   |  [link](https://drive.google.com/file/d/1u1ScUMdlOfyIyUOIcZBonIUb7rXJwGH8/view)  |  [link](https://drive.google.com/file/d/1blW_lXnUFa3poUwR6YuHd3N2fVoGuHhG/view)
zho   |  [link](https://drive.google.com/file/d/10ipmN3CgNFXc6OQst6-Iasa5CaZLT93M/view)  |  [link](https://drive.google.com/file/d/13-qysDM2uAiT_E9KjAKsQZAQP_-0pyRL/view)
bis   |  -                                                                               |  [link](https://drive.google.com/file/d/1zUn6LDov0zi_hxYbs9hX63UwLhcNcrsa/view)
gla   |  -                                                                               |  [link](https://drive.google.com/file/d/1rIYRlZQ0Sl6By45hdOozAS_37Dv6LFQp/view)

## Cite Us!
Please cite us if you use our data or methodology 
```
@inproceedings{varab-schluter-2021-massivesumm,
    title = "{M}assive{S}umm: a very large-scale, very multilingual, news summarisation dataset",
    author = "Varab, Daniel  and
      Schluter, Natalie",
    booktitle = "Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing",
    month = nov,
    year = "2021",
    address = "Online and Punta Cana, Dominican Republic",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.emnlp-main.797",
    pages = "10150--10161",
    abstract = "Current research in automatic summarisation is unapologetically anglo-centered{--}a persistent state-of-affairs, which also predates neural net approaches. High-quality automatic summarisation datasets are notoriously expensive to create, posing a challenge for any language. However, with digitalisation, archiving, and social media advertising of newswire articles, recent work has shown how, with careful methodology application, large-scale datasets can now be simply gathered instead of written. In this paper, we present a large-scale multilingual summarisation dataset containing articles in 92 languages, spread across 28.8 million articles, in more than 35 writing scripts. This is both the largest, most inclusive, existing automatic summarisation dataset, as well as one of the largest, most inclusive, ever published datasets for any NLP task. We present the first investigation on the efficacy of resource building from news platforms in the low-resource language setting. Finally, we provide some first insight on how low-resource language settings impact state-of-the-art automatic summarisation system performance.",
}
```
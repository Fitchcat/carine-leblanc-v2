urls=(
"https://d1yei2z3i6k35z.cloudfront.net/3226424/65564eb47a027_piggy-moneybox-with-euro-cash-2021-08-26-17-02-21-utc.jpg"
"https://d1yei2z3i6k35z.cloudfront.net/3226424/65f2c78bf0773_logoCarine.png"
"https://d1yei2z3i6k35z.cloudfront.net/3226424/65f2e6ed3785c_logoCarineWhite.png"
"https://d1yei2z3i6k35z.cloudfront.net/3226424/65f3064c123e6_quotidien.webp"
"https://d1yei2z3i6k35z.cloudfront.net/3226424/65f3065b7326d_Evenement.webp"
"https://d1yei2z3i6k35z.cloudfront.net/3226424/65f306674c4e4_Loisirs.webp"
"https://d1yei2z3i6k35z.cloudfront.net/3226424/65f306798298c_Relocation.webp"
"https://d1yei2z3i6k35z.cloudfront.net/3226424/65f31128a547e_PanneauCarine.png"
"https://d1yei2z3i6k35z.cloudfront.net/3226424/65f3600a8f7c5_CarineFaceBW.png"
"https://d1yei2z3i6k35z.cloudfront.net/3226424/65f4858319a7e_logoCarine.png"
"https://d1yei2z3i6k35z.cloudfront.net/3226424/65f4859c4aa86_logoCarine.png"
"https://d1yei2z3i6k35z.cloudfront.net/3226424/68d7a3f7a7bfe_replicate-prediction-sb9kb7f8ssrme0csh9bv0v445r.jpg"
"https://d1yei2z3i6k35z.cloudfront.net/3226424/68d7a7fb86429_replicate-prediction-szsks2w3qdrm80csh9krxffch4.jpg"
"https://d1yei2z3i6k35z.cloudfront.net/systeme-common/63a1ca26281bf_Web192012.jpg"
)
for url in "${urls[@]}"; do
  curl -s -O "$url"
done

from probability import bayes_binary
# lib:farmer
# H 1:17

# E(d) = person likes working alone in quiet space
# E(l) = 40%     E(F) = 10%

# P(A|B) = P(B|A) * P(A) / P(B)
# 𝑃(𝐵)=𝑃(𝐵∣𝐴)𝑃(𝐴)+𝑃(𝐵∣¬𝐴)𝑃(¬𝐴)

print(f"org: {1/17*100:.1f}%")
print(f"{bayes_binary(1/17, 0.4, 0.1)*100:.1f}%")
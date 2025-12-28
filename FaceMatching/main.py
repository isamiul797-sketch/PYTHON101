from deepface import DeepFace

# result = DeepFace.verify("t1.jpg","t2.webp")
# print(result)



# result = DeepFace.analyze(
#     img_path="t1.jpg",
#     actions=["age","gender","emotion","race"]
# )

# print(result)


result = DeepFace.analyze(
    img_path="g00.avif",
    detector_backend="retinaface",
    enforce_detection=True
)

print(result)
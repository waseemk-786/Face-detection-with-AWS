from urllib import response
import streamlit as st
import boto3

st.title('face recogonising using AWS')
img_file=st.file_uploader('upload face image',type=['png','jpg','jpeg'])
if img_file is not None:
    file_details={}
    file_details['name']=img_file.name
    file_details['type']=img_file.type
    file_details['size']=img_file.size
    st.write(file_details)

    with open('input.jpg','wb') as f:
        f.write(img_file.getbuffer())
    
    client=boto3.client('rekognition')
    imageSource=open('input.jpg','rb')
    imageTarget=open('waseem.jpg','rb')

    response=client.compare_faces(
        SimilarityThreshold=70,
        SourceImage={'Bytes':imageSource.read()},
        TargetImage={'Bytes':imageTarget.read()}
    )
    #st.write(response)
    if (len(response['FaceMatches'])>0):
        st.success('Face Matched')
    else:
        st.error('Face not Matched')
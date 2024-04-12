import streamlit as st
import joblib
import pandas as pd
import sys
import webbrowser

sys.path.append("/mount/src/estatelookout.ai/model")
from Listing_Model import Listing_Model


PROPERTY_DATA_FILE = "/mount/src/estatelookout.ai/data"

def load_listings(search_query: str, sale_type=None, num_beds=None):
    
    model = joblib.load("/mount/src/estatelookout.ai/model/listing_model.pkl")
    # Make predictions
    similarity = model.predict(search_query)
    property_df = pd.read_csv(PROPERTY_DATA_FILE)
    
    property_df = property_df.set_index('id').reset_index()

    
    # filter results 
    if sale_type:
        similarity= similarity[property_df.sale_type==sale_type]
    if sale_type == "rent":
        minp=min(property_df.price_in_aed.loc[property_df.sale_type==sale_type])
        maxp = max(property_df.price_in_aed.loc[property_df.sale_type==sale_type])
        
        
        
        price_range_rent = st.sidebar.slider("Price Range (AED) per Annum", min_value = minp ,max_value=maxp, value=(minp,maxp))
        min_price,max_price  = price_range_rent
        
        similarity = similarity[(max_price >= property_df.loc[similarity.index, 'price_in_aed']) & (property_df.loc[similarity.index, 'price_in_aed'] >= min_price)]

        # similarity = similarity[(max_price>=property_df.price_in_aed) & (property_df.price_in_aed>=min_price)]
        
    else:
        minp=min(property_df.price_in_aed.loc[property_df.sale_type==sale_type])
        maxp = max(property_df.price_in_aed.loc[property_df.sale_type==sale_type])
        
        price_range_sale = st.sidebar.slider("Price Range (AED)", min_value = minp ,max_value=maxp, value=(minp,maxp))
        min_price,max_price  = price_range_sale
        
 

        similarity = similarity[(max_price >= property_df.loc[similarity.index, 'price_in_aed']) & (property_df.loc[similarity.index, 'price_in_aed'] >= min_price)]
    
        # similarity = similarity[(max_price>=property_df.price_in_aed) & (property_df.price_in_aed>=min_price)]
    
    
    if num_beds and num_beds!="any":
        similarity = similarity[property_df.number_of_beds==num_beds]   
    
    if st.sidebar.button("Visit Main Site"):
        # webbrowser.open_new_tab("https://www.allsoppandallsopp.com/") ## for auto-redirect
        st.sidebar.write("https://www.allsoppandallsopp.com/")


    return similarity


    
    
    
def display_results(df):
    df_contact = pd.read_csv("/mount/src/estatelookout.ai/data/contact_data.csv")

    df_contact.drop("Unnamed: 0",axis=1)
    df_contact['similarity']=df.similarity_score
    
    df_contact = df_contact.loc[df.index]

    for index, row in df_contact[:100].iterrows():   # only display 100 results
        st.write('---')
        col1, col2 = st.columns([1, 4])  
        with col1:
                st.image(row['image_url'], caption=row['summary'], use_column_width=True)


        with col2:
            st.write(f"**Price: AED** {row['price_in_aed']:,}")
            st.write(f"**Price: $** {round(row['price_in_aed']/3.65):,}" )

            st.write(f"**Location:** {row['location']}")
            st.write(f"**Description:** {row['title']}")
            st.write(f"**Number of Bedrooms** {row['number_of_beds']}")
            st.write(f"**Sale Type** {row['sale_type']}")
            
            st.write(f"**Similarity:** {row['similarity']:.2}")
            
            if st.button(f'Call Agent {index+1}: **{row["agent_name"]}** '):
                # webbrowser.open_new_tab(row['call_agent'])
                st.write(row['call_agent'])


            if st.button(f'View Details {index+1}'):
                # webbrowser.open_new_tab(row['page_url'])
                st.write(row['page_url'])

            

    
    
    
    
def main():
    st.set_page_config(page_title="Dream Home Search", page_icon="🏠", layout="wide")

    st.markdown("<h1 style='text-align: center; color: white;'>Find Your Dream Home</h1>", unsafe_allow_html=True)
    col1,col2,col3= st.columns(3)
    with col2:
        search_query = st.text_input("Describe Your Dream Home!")



    
    sale_type = st.sidebar.selectbox("sale_type",options=["buy","rent"])
    
    num_beds = st.sidebar.selectbox("Select Number of Bedrooms", options=["any",1,2,3,4,5,6,7])

    # Display the centered button in the sidebar

    df = load_listings(search_query,sale_type=sale_type,num_beds=num_beds)

    display_results(df)
    
    
    
    
    
    
    
    
if __name__ == "__main__" :
    main()
    
    
 

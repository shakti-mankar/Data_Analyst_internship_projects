
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# =====================================================
# 1. PAGE CONFIGURATION
# =====================================================

st.set_page_config(
    page_title="Real Estate Investment Advisor",
    page_icon="🏠",
    layout="wide"
)


# =====================================================
# 2. LOAD CLEANED DATASET
# =====================================================

@st.cache_data
def load_data():
    return pd.read_csv("data/cleaned_housing_data.csv")


df = load_data()


# =====================================================
# 3. APPLICATION TITLE
# =====================================================

st.title("🏠 Real Estate Investment Advisor")

st.write(
    "Explore Indian housing data through interactive "
    "charts, tables, and property analysis."
)

st.divider()


# =====================================================
# 4. SIDEBAR NAVIGATION
# =====================================================

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Select Dashboard Section",
    [
        "Dashboard Overview",
        "Property Analysis",
        "Location Analysis",
        "Investment Insights",
        "Property Search",
        "Property Comparison"
    ]
)

st.sidebar.divider()


# =====================================================
# 5. SIDEBAR FILTERS
# =====================================================

st.sidebar.header("Property Filters")

# State filter
states = ["All"] + sorted(
    df["State"].dropna().unique().tolist()
)

selected_state = st.sidebar.selectbox(
    "Select State",
    states
)

# Apply state filter
if selected_state != "All":
    filtered_df = df[df["State"] == selected_state].copy()
else:
    filtered_df = df.copy()


# City filter
cities = ["All"] + sorted(
    filtered_df["City"].dropna().unique().tolist()
)

selected_city = st.sidebar.selectbox(
    "Select City",
    cities
)

if selected_city != "All":
    filtered_df = filtered_df[
        filtered_df["City"] == selected_city
    ]


# Property type filter
property_types = ["All"] + sorted(
    df["Property_Type"].dropna().unique().tolist()
)

selected_property = st.sidebar.selectbox(
    "Select Property Type",
    property_types
)

if selected_property != "All":
    filtered_df = filtered_df[
        filtered_df["Property_Type"] == selected_property
    ]


# =====================================================
# 6. MAIN DASHBOARD
# =====================================================

st.header(page)

st.write(
    f"Showing **{len(filtered_df):,}** properties "
    "based on your selected filters."
)

st.divider()


if filtered_df.empty:

    st.warning(
        "No properties found for the selected filters. "
        "Please change your filters."
    )

else:

    # =================================================
    # 7. KEY PERFORMANCE INDICATORS
    # =================================================

    st.subheader("Key Performance Indicators")

    valid_price_per_sqft = filtered_df.loc[
        filtered_df["Price_per_SqFt"] > 0,
        "Price_per_SqFt"
    ]

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Total Properties",
            f"{len(filtered_df):,}"
        )

    with col2:
        st.metric(
            "Average Property Price",
            f"₹{filtered_df['Price_in_Lakhs'].mean():.2f} Lakhs"
        )

    with col3:
        st.metric(
            "Median Property Price",
            f"₹{filtered_df['Price_in_Lakhs'].median():.2f} Lakhs"
        )

    with col4:
        if not valid_price_per_sqft.empty:
            average_price_sqft = valid_price_per_sqft.mean() * 100000

            st.metric(
                "Average Price per SqFt",
                f"₹{average_price_sqft:,.0f}"
            )
        else:
            st.metric(
                "Average Price per SqFt",
                "N/A"
            )

    st.divider()


    # =================================================
    # 8. ADDITIONAL PROPERTY STATISTICS
    # =================================================

    st.subheader("Property Statistics")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Average Property Size",
            f"{filtered_df['Size_in_SqFt'].mean():.0f} SqFt"
        )

    with col2:
        st.metric(
            "Average BHK",
            f"{filtered_df['BHK'].mean():.1f}"
        )

    with col3:
        st.metric(
            "Average Property Age",
            f"{filtered_df['Age_of_Property'].mean():.1f} Years"
        )

    st.divider()


    # =================================================
    # 9. DASHBOARD OVERVIEW
    # =================================================

    if page == "Dashboard Overview":

        st.subheader("Housing Dataset Preview")

        st.dataframe(
            filtered_df.head(20),
            use_container_width=True
        )


    # =================================================
    # 10. PROPERTY ANALYSIS
    # =================================================

    elif page == "Property Analysis":

        st.subheader("Property Price Analysis")

        # ---------------------------------------------
        # Chart 1: Property Price Distribution
        # ---------------------------------------------

        st.markdown("### 1. Distribution of Property Prices")

        fig_price = px.histogram(
            filtered_df,
            x="Price_in_Lakhs",
            nbins=30,
            title="Distribution of Property Prices",
            labels={
                "Price_in_Lakhs": "Property Price (Lakhs)",
                "count": "Number of Properties"
            }
        )

        st.plotly_chart(
            fig_price,
            use_container_width=True
        )

        st.caption(
            "This chart shows how property prices are "
            "distributed across the selected properties."
        )

        st.divider()


        # ---------------------------------------------
        # Chart 2: Average Price by Property Type
        # ---------------------------------------------

        st.markdown("### 2. Average Price by Property Type")

        property_price = (
            filtered_df.groupby("Property_Type")["Price_in_Lakhs"]
            .mean()
            .reset_index()
            .sort_values(
                "Price_in_Lakhs",
                ascending=False
            )
        )

        fig_property = px.bar(
            property_price,
            x="Property_Type",
            y="Price_in_Lakhs",
            title="Average Property Price by Property Type",
            labels={
                "Property_Type": "Property Type",
                "Price_in_Lakhs": "Average Price (Lakhs)"
            },
            text_auto=".2f"
        )

        st.plotly_chart(
            fig_property,
            use_container_width=True
        )

        st.caption(
            "This chart compares average property prices "
            "across different property categories."
        )

        st.divider()


        # ---------------------------------------------
        # Chart 3: Property Size vs Property Price
        # ---------------------------------------------

        st.markdown("### 3. Property Size vs Property Price")

        chart_data = filtered_df.sample(
            n=min(5000, len(filtered_df)),
            random_state=42
        )

        fig_scatter = px.scatter(
            chart_data,
            x="Size_in_SqFt",
            y="Price_in_Lakhs",
            color="Property_Type",
            title="Relationship Between Property Size and Price",
            labels={
                "Size_in_SqFt": "Property Size (SqFt)",
                "Price_in_Lakhs": "Property Price (Lakhs)"
            },
            opacity=0.6
        )

        st.plotly_chart(
            fig_scatter,
            use_container_width=True
        )

        st.caption(
            "This chart helps visualize how property prices "
            "vary with property size."
        )

        st.divider()


        # Property data table
        st.subheader("Property Records")

        st.dataframe(
            filtered_df.head(20),
            use_container_width=True
        )


    # =================================================
    # 11. LOCATION ANALYSIS
    # =================================================


    elif page == "Location Analysis":

        st.subheader("Real Estate Location Analysis")

        # ---------------------------------------------
        # Chart 1: Average Property Price by State
        # ---------------------------------------------

        st.markdown("### 1. Average Property Price by State")

        state_price = (
            filtered_df.groupby("State")["Price_in_Lakhs"]
            .mean()
            .reset_index()
            .sort_values(
                "Price_in_Lakhs",
                ascending=False
            )
        )

        fig_state = px.bar(
            state_price,
            x="State",
            y="Price_in_Lakhs",
            title="Average Property Price by State",
            labels={
                "State": "State",
                "Price_in_Lakhs": "Average Price (Lakhs)"
            },
            text_auto=".2f"
        )

        st.plotly_chart(
            fig_state,
            use_container_width=True
        )

        st.divider()


        # ---------------------------------------------
        # Chart 2: Average Property Price by City
        # ---------------------------------------------

        st.markdown("### 2. Average Property Price by City")

        city_price = (
            filtered_df.groupby("City")["Price_in_Lakhs"]
            .mean()
            .reset_index()
            .sort_values(
                "Price_in_Lakhs",
                ascending=False
            )
        )

        top_cities = city_price.head(15)

        fig_city = px.bar(
            top_cities,
            x="City",
            y="Price_in_Lakhs",
            title="Top 15 Cities by Average Property Price",
            labels={
                "City": "City",
                "Price_in_Lakhs": "Average Price (Lakhs)"
            },
            text_auto=".2f"
        )

        st.plotly_chart(
            fig_city,
            use_container_width=True
        )

        st.divider()


        # ---------------------------------------------
        # Chart 3: Average Price per SqFt by State
        # ---------------------------------------------

        st.markdown("### 3. Average Price per SqFt by State")

        state_sqft = (
            filtered_df[
                filtered_df["Price_per_SqFt"] > 0
            ]
            .groupby("State")["Price_per_SqFt"]
            .mean()
            .reset_index()
            .sort_values(
                "Price_per_SqFt",
                ascending=False
            )
        )

        # Convert lakhs per SqFt into rupees per SqFt
        state_sqft["Price_per_SqFt_Rupees"] = (
            state_sqft["Price_per_SqFt"] * 100000
        )

        fig_sqft = px.bar(
            state_sqft,
            x="State",
            y="Price_per_SqFt_Rupees",
            title="Average Price per SqFt by State",
            labels={
                "State": "State",
                "Price_per_SqFt_Rupees": "Average Price (₹ per SqFt)"
            },
            text_auto=",.0f"
        )

        st.plotly_chart(
            fig_sqft,
            use_container_width=True
        )

        st.divider()


        # ---------------------------------------------
        # Location Summary Table
        # ---------------------------------------------

        st.subheader("Location Price Summary")

        location_summary = (
            filtered_df.groupby(["State", "City"])
            .agg(
                Average_Price=("Price_in_Lakhs", "mean"),
                Median_Price=("Price_in_Lakhs", "median"),
                Property_Count=("ID", "count")
            )
            .reset_index()
            .sort_values(
                "Average_Price",
                ascending=False
            )
        )

        st.dataframe(
            location_summary,
            use_container_width=True
        )

        # ---------------------------------------------
        # Highest and Lowest Average Price Cities
        # ---------------------------------------------

        if not city_price.empty:

            highest_city = city_price.iloc[0]
            lowest_city = city_price.iloc[-1]

            st.subheader("Location Highlights")

            col1, col2 = st.columns(2)

            with col1:
                st.metric(
                    "Highest Average Price City",
                    highest_city["City"],
                    f"₹{highest_city['Price_in_Lakhs']:.2f} Lakhs"
                )

            with col2:
                st.metric(
                    "Lowest Average Price City",
                    lowest_city["City"],
                    f"₹{lowest_city['Price_in_Lakhs']:.2f} Lakhs"
                )


    # =================================================
    # 12. INVESTMENT INSIGHTS
    # =================================================


    elif page == "Investment Insights":

        st.subheader("Property Investment Insights")

        st.write(
            "Compare property characteristics and understand "
            "how they are associated with property prices."
        )

        # ---------------------------------------------
        # Chart 1: Property Age vs Average Price
        # ---------------------------------------------

        st.markdown("### 1. Property Age Analysis")

        age_data = filtered_df.copy()

        age_data["Age_Group"] = pd.cut(
            age_data["Age_of_Property"],
            bins=[-1, 5, 10, 20, 30, float("inf")],
            labels=[
                "0-5 Years",
                "6-10 Years",
                "11-20 Years",
                "21-30 Years",
                "Above 30 Years"
            ]
        )

        age_summary = (
            age_data.groupby("Age_Group", observed=False)
            ["Price_in_Lakhs"]
            .mean()
            .reset_index()
        )

        fig_age = px.bar(
            age_summary,
            x="Age_Group",
            y="Price_in_Lakhs",
            title="Average Property Price by Property Age",
            labels={
                "Age_Group": "Property Age",
                "Price_in_Lakhs": "Average Price (Lakhs)"
            },
            text_auto=".2f"
        )

        st.plotly_chart(
            fig_age,
            use_container_width=True
        )

        st.divider()


        # ---------------------------------------------
        # Chart 2: Furnishing Status vs Price
        # ---------------------------------------------

        st.markdown("### 2. Furnishing Status Analysis")

        furnishing_summary = (
            filtered_df.groupby("Furnished_Status")
            ["Price_in_Lakhs"]
            .mean()
            .reset_index()
            .sort_values("Price_in_Lakhs", ascending=False)
        )

        fig_furnishing = px.bar(
            furnishing_summary,
            x="Furnished_Status",
            y="Price_in_Lakhs",
            title="Average Property Price by Furnishing Status",
            labels={
                "Furnished_Status": "Furnishing Status",
                "Price_in_Lakhs": "Average Price (Lakhs)"
            },
            text_auto=".2f"
        )

        st.plotly_chart(
            fig_furnishing,
            use_container_width=True
        )

        st.divider()


        # ---------------------------------------------
        # Chart 3: Parking Space vs Price
        # ---------------------------------------------

        st.markdown("### 3. Parking Space Analysis")

        parking_summary = (
            filtered_df.groupby("Parking_Space")
            ["Price_in_Lakhs"]
            .mean()
            .reset_index()
            .sort_values("Price_in_Lakhs", ascending=False)
        )

        fig_parking = px.bar(
            parking_summary,
            x="Parking_Space",
            y="Price_in_Lakhs",
            title="Average Property Price by Parking Space",
            labels={
                "Parking_Space": "Parking Availability",
                "Price_in_Lakhs": "Average Price (Lakhs)"
            },
            text_auto=".2f"
        )

        st.plotly_chart(
            fig_parking,
            use_container_width=True
        )

        st.divider()


        # ---------------------------------------------
        # Chart 4: Public Transport Accessibility
        # ---------------------------------------------

        st.markdown("### 4. Public Transport Accessibility")

        transport_data = filtered_df[
            filtered_df["Price_per_SqFt"] > 0
        ]

        transport_summary = (
            transport_data.groupby("Public_Transport_Accessibility")
            ["Price_per_SqFt"]
            .mean()
            .reset_index()
            .sort_values("Price_per_SqFt", ascending=False)
        )

        transport_summary["Price_Rupees_Per_SqFt"] = (
            transport_summary["Price_per_SqFt"] * 100000
        )

        fig_transport = px.bar(
            transport_summary,
            x="Public_Transport_Accessibility",
            y="Price_Rupees_Per_SqFt",
            title="Average Price per SqFt by Transport Accessibility",
            labels={
                "Public_Transport_Accessibility": "Transport Accessibility",
                "Price_Rupees_Per_SqFt": "Average Price (₹ per SqFt)"
            },
            text_auto=",.0f"
        )

        st.plotly_chart(
            fig_transport,
            use_container_width=True
        )

        st.divider()


        # ---------------------------------------------
        # Chart 5: Amenities Analysis
        # ---------------------------------------------

        st.markdown("### 5. Amenities Analysis")

        amenities_data = filtered_df[
            ["Amenities", "Price_per_SqFt"]
        ].copy()

        amenities_data["Amenities"] = (
            amenities_data["Amenities"]
            .fillna("")
            .astype(str)
            .str.split(",")
        )

        amenities_data = amenities_data.explode("Amenities")

        amenities_data["Amenities"] = (
            amenities_data["Amenities"].str.strip()
        )

        amenities_data = amenities_data[
            (amenities_data["Amenities"] != "") &
            (amenities_data["Price_per_SqFt"] > 0)
        ]

        if not amenities_data.empty:

            amenities_summary = (
                amenities_data.groupby("Amenities")
                ["Price_per_SqFt"]
                .agg(["mean", "count"])
                .reset_index()
            )

            amenities_summary.columns = [
                "Amenity",
                "Average_Price_Per_SqFt",
                "Property_Count"
            ]

            # Keep amenities with at least 5 records
            amenities_summary = amenities_summary[
                amenities_summary["Property_Count"] >= 5
            ]

            amenities_summary = amenities_summary.sort_values(
                "Average_Price_Per_SqFt",
                ascending=False
            ).head(10)

            amenities_summary["Average_Price_Rupees"] = (
                amenities_summary["Average_Price_Per_SqFt"] * 100000
            )

            if not amenities_summary.empty:

                fig_amenities = px.bar(
                    amenities_summary,
                    x="Amenity",
                    y="Average_Price_Rupees",
                    title="Top 10 Amenities by Average Price per SqFt",
                    labels={
                        "Amenity": "Amenity",
                        "Average_Price_Rupees": "Average Price (₹ per SqFt)"
                    },
                    text_auto=",.0f"
                )

                st.plotly_chart(
                    fig_amenities,
                    use_container_width=True
                )

                st.dataframe(
                    amenities_summary,
                    use_container_width=True
                )

            else:
                st.info(
                    "There are not enough amenity records "
                    "to display this comparison."
                )

        else:
            st.info("No valid amenity data is available.")

        st.divider()

        st.warning(
            "These comparisons show associations in the dataset. "
            "They do not establish causation, actual investment "
            "profitability, or future property value."
        )





    # =================================================
    # 13. INTERACTIVE PROPERTY SEARCH
    # =================================================

    elif page == "Property Search":

        st.subheader("Find Your Ideal Property")

        st.write(
            "Search properties according to your budget, "
            "bedroom requirements, and preferred property size."
        )

        st.divider()

        # ---------------------------------------------
        # Search Filters
        # ---------------------------------------------

        st.markdown("### Set Your Property Preferences")

        col1, col2 = st.columns(2)

        with col1:

            min_budget = float(filtered_df["Price_in_Lakhs"].min())
            max_budget = float(filtered_df["Price_in_Lakhs"].max())

            budget_range = st.slider(
                "Select Your Budget (Lakhs)",
                min_value=min_budget,
                max_value=max_budget,
                value=(min_budget, max_budget),
                step=1.0
            )

            available_bhk = sorted(
                filtered_df["BHK"].dropna().unique().tolist()
            )

            selected_bhk = st.multiselect(
                "Select BHK",
                available_bhk,
                default=available_bhk
            )

        with col2:

            min_size = int(filtered_df["Size_in_SqFt"].min())
            max_size = int(filtered_df["Size_in_SqFt"].max())

            size_range = st.slider(
                "Select Property Size (SqFt)",
                min_value=min_size,
                max_value=max_size,
                value=(min_size, max_size)
            )

            available_furnishing = sorted(
                filtered_df["Furnished_Status"]
                .dropna()
                .unique()
                .tolist()
            )

            selected_furnishing = st.multiselect(
                "Furnishing Status",
                available_furnishing,
                default=available_furnishing
            )

        st.divider()

        # ---------------------------------------------
        # Search Button
        # ---------------------------------------------

        if st.button(
            "Search Properties",
            type="primary",
            use_container_width=True
        ):

            search_results = filtered_df[
                (filtered_df["Price_in_Lakhs"] >= budget_range[0]) &
                (filtered_df["Price_in_Lakhs"] <= budget_range[1]) &
                (filtered_df["Size_in_SqFt"] >= size_range[0]) &
                (filtered_df["Size_in_SqFt"] <= size_range[1]) &
                (filtered_df["BHK"].isin(selected_bhk)) &
                (filtered_df["Furnished_Status"].isin(selected_furnishing))
            ].copy()

            st.session_state["property_search_results"] = search_results

        # ---------------------------------------------
        # Display Search Results
        # ---------------------------------------------

        if "property_search_results" in st.session_state:

            search_results = st.session_state[
                "property_search_results"
            ]

            st.subheader("Property Search Results")

            st.metric(
                "Matching Properties",
                f"{len(search_results):,}"
            )

            if not search_results.empty:

                st.success(
                    f"Found {len(search_results):,} matching properties."
                )

                display_columns = [
                    "ID",
                    "State",
                    "City",
                    "Locality",
                    "Property_Type",
                    "BHK",
                    "Size_in_SqFt",
                    "Price_in_Lakhs",
                    "Furnished_Status",
                    "Parking_Space"
                ]

                st.dataframe(
                    search_results[display_columns],
                    use_container_width=True
                )

                # Download search results
                csv_data = search_results.to_csv(
                    index=False
                ).encode("utf-8")

                st.download_button(
                    label="Download Matching Properties",
                    data=csv_data,
                    file_name="property_search_results.csv",
                    mime="text/csv"
                )

            else:

                st.warning(
                    "No properties match your selected preferences. "
                    "Try increasing your budget or changing your filters."
                )






    # =================================================
    # PROPERTY COMPARISON
    # =================================================

    elif page == "Property Comparison":

        st.subheader("Compare Properties")

        st.write(
            "Enter property IDs to compare their prices, sizes, "
            "locations, and other important features."
        )

        st.info(
            "You can find Property IDs in the Dashboard Overview "
            "or Property Search results."
        )

        property_ids = st.text_input(
            "Enter Property IDs separated by commas",
            placeholder="Example: 101, 102, 103"
        )

        if st.button("Compare Properties", type="primary"):

            requested_ids = [
                item.strip()
                for item in property_ids.split(",")
                if item.strip()
            ]

            comparison_df = filtered_df[
                filtered_df["ID"].astype(str).isin(requested_ids)
            ].copy()

            st.session_state["comparison_results"] = comparison_df

        if "comparison_results" in st.session_state:

            comparison_df = st.session_state["comparison_results"]

            st.divider()

            if len(comparison_df) >= 2:

                st.success(
                    f"Comparing {len(comparison_df)} properties."
                )

                comparison_df["Price_Rupees_Per_SqFt"] = (
                    comparison_df["Price_per_SqFt"] * 100000
                )

                comparison_columns = [
                    "ID",
                    "State",
                    "City",
                    "Locality",
                    "Property_Type",
                    "BHK",
                    "Size_in_SqFt",
                    "Price_in_Lakhs",
                    "Price_Rupees_Per_SqFt",
                    "Age_of_Property",
                    "Furnished_Status",
                    "Parking_Space",
                    "Public_Transport_Accessibility"
                ]

                st.subheader("Property Details")

                st.dataframe(
                    comparison_df[comparison_columns],
                    use_container_width=True,
                    hide_index=True
                )

                st.subheader("Price Comparison")

                price_chart = px.bar(
                    comparison_df,
                    x="ID",
                    y="Price_in_Lakhs",
                    color="Property_Type",
                    title="Property Price Comparison",
                    labels={
                        "ID": "Property ID",
                        "Price_in_Lakhs": "Price (Lakhs)"
                    }
                )

                st.plotly_chart(
                    price_chart,
                    use_container_width=True
                )

                st.subheader("Property Size Comparison")

                size_chart = px.bar(
                    comparison_df,
                    x="ID",
                    y="Size_in_SqFt",
                    color="Property_Type",
                    title="Property Size Comparison",
                    labels={
                        "ID": "Property ID",
                        "Size_in_SqFt": "Size (SqFt)"
                    }
                )

                st.plotly_chart(
                    size_chart,
                    use_container_width=True
                )

            elif len(comparison_df) == 1:

                st.warning(
                    "Only one matching property was found. "
                    "Please enter at least two valid Property IDs."
                )

            else:

                st.warning(
                    "No matching properties found. Check the IDs "
                    "and your selected sidebar filters."
                )



# =====================================================
# 13. FOOTER
# =====================================================

st.divider()

st.caption(
    "Real Estate Investment Advisor | "
    "Python, Pandas, Plotly and Streamlit"
)

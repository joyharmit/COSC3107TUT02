def get_page_html(form_data):
    print("About to return Student Y page...")
    page_html="""
        <!DOCTYPE html>
        <html>

        <head>
            <!-- Include the external css file -->
            <link rel="stylesheet" href="style.css">
        </head>

        <body>

            <div class="topnav">
                <a href="/">Homepage (Student X)</a>
                <a href="/studenty">Student Y</a>
            </div>

            <div class="header">
                <h1>
                    <img src="tmp-image.png" class="top-image" alt="logo" width="75" height="75">
                    Programming Class 5 exercise Student Y page
                </h1>
            </div>

            <div class="content">
                <p>Content</p>
            </div>

            <div class="footer">
                <p>COSC3106 - Programming Class 5</p>
            </div>

        </body>
        </html>
    

    """
    return page_html

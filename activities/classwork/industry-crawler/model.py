class AbstractIndustry(object):


    def __init__(self, title, children):
        logger.info("Creating Industry_ {title}".format(title=title))
        self.title = title
        self.children = children



    def level(self):
        raise NotImplementedError("Abstract industry does not contains level.")


    def add_child(self, child):
        self.children.append(child)


    def to_dict(self):
        return{
            "title": self.title,
            "children": [child.to_dict() for child in self.children]
        }


    def jsonify(self):
    def from_url(url):
        response = requests.get(url)
        html = BeautifulSoup(response.text, 'html.parser')
        return MajorGroup(
            title=[elm.text for elm in html.find_all("h2") if elm.text.lower().startswith("major group")][0],	            title=[

            children=[
                Group(
                    title=group.text,
                    children=[
                        Single(
                            title=f"{inner.parent.text}",
                            children=[]
                        )	                        )
                        for inner in html.find_all("a")
                        if inner.attrs.get("href", "").startswith("sic_manual")
                        and inner.parent.text.startswith(group.text.split(":")[0].split(" ")[-1])
                    ]	                    ]
                )	                )
                for group in html.find_all("strong") if group.text.lower().startswith("industry group")
            ]	            ]
        )	        )



class Group(AbstractIndustry):
    level = "SIC Group"


class SIC(AbstractIndustry):
    @staticmethod
    def load_json(filename):
        with open(filename, "r") as file:
            sic_industries = json.load(file.read())
        return sic_industries


    @staticmethod
    def from_url(url):

            elif href.endswith("group"):
                major_group_url = url.replace("sic_manual.html", href)
                divisions[-1].add_child(MajorGroup.from_url(major_group_url))
        return Single(
            title="SIC",
            children=divisions
        )


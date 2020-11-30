def setup():
    title = "fruity photos"
    sophie = "https://github.com/sophieleeajh"
    linda = "https://github.com/lindalonglong"
    maggie = "https://github.com/maggie3000"
    adam = "https://github.com/AdamHolbel"
    wenshi = "https://github.com/wenshibao"    
    sophievid = "https://youtu.be/aPTJ5J0kxi0"
    lindavid = "https://www.youtube.com/watch?v=lu6bdBbVXh4"
    maggievid = "/"    
    adamvid = "/"
    wenshivid = "/"
    triojournal = "https://docs.google.com/spreadsheets/d/1elSgQhDFkBvTvTqnRh8zs0XKX0BS7Nr3QeHGaYTkk0k/edit?ouid=115921679004469073625&usp=sheets_home&ths=true"
    pairjournal = "https://docs.google.com/document/d/1L9sVv2iMl7lLbC6PNYKWoeHRtvyGecbl9zUvXjIErNA/edit?usp=sharing"

    source = {"title": title, "sophie": sophie, "linda": linda, "maggie": maggie, "adam": adam, "wenshi": wenshi, "sophievid": sophievid, "lindavid": lindavid, "maggievid": maggievid, "adamvid": adamvid, "wenshivid": wenshivid, "triojournal": triojournal, "pairjourna": pairjournal}

    return title

    project1 = "Hello Series"
    projlinks1 = [
        Link("Project Plan", ""),
        Link("Repl", ""),
    ]
    project2 =  "Flask Project"
    projlinks2 = [
        Link("Project Plan", ""),
        Link("Repl", ""),
    ]

    proj1 = Project(project1, projlinks1)
    proj2 = Project(project2, projlinks2)

    projects = Projects(source, [proj1, proj2])
    return projects

class Link():
    def __init__(self, btn, href):
        self.btn = btn
        self.href = href
    def get_btn(self):
        return self.btn
    def get_href(self):
        return self.href

class Project():
    def __init__(self, name, links):
        self.name = name
        self.links = links
    def get_name(self):
        return self.name
    def get_links(self):
        return self.links

class Projects():
    def __init__(self, source, projects):
        self.source = source
        self.projects = projects
    def get_source(self):
        return self.source
    def get_projects(self):
        return self.projects

from django.test import TestCase
from Tracker import views, scraper

none = ""
google = "https://www.google.com/"
linkedin = "https://www.linkedin.com/feed/"
ziprecruiter = "https://www.ziprecruiter.com/jobseeker/home"
indeed = "https://www.indeed.com/"
glassdoor = "https://www.glassdoor.com/Community/index.htm"
job1 = "https://www.ziprecruiter.com/ojob/wealthcounsel-llc/junior-software-developer?lvk=r6DG5EgCLN6AqXIkqFJDBQ.--Nq8yUtUN7&zrclid=837ba598-fc58-41c1-86b1-121d96775e1f"
job2 = "https://www.glassdoor.com/Job/philadelphia-pa-us-junior-software-engineer-jobs-SRCH_IL.0,18_IC1152672_KO19,43.htm"
job3 = "https://www.indeed.com/viewjob?jk=1098266a620fb189&q=corporate+trainer&tk=1isc4nbf0ljdq801&from=hpd.jobsForYou&advn=5808625144900202&adid=446278998&ad=-6NYlbfkN0DRc4F8Q0at8t3mDfkSjGSU3K4Uez2oWQqM_R660bb0MnbxVKFBgTK1ew_wQgcKhQFIOjNng5gCElVp3qOCfw-vERGHzr5bvMGoVV54p0rNvxK6Sg4ZLGs4hLiI1r6siDA6_b7IEyJCsaQbk401BjWLctDMLVWGXi0yabg44U75l5a6QR2jrMhA9_yikXSPIXfRVlSBqNLHc9uRoSLrJS3a1zl4B-UYiejrFEMkKtoXpVbEIp90TUBl-KAiG_-9_UUqwJ9gC3PJPxSvzJ4IUAJ3pRt54KWPRlOGmGIreV03sHkc-LJG0GITmQjDgls9R6lw-cy1KECxrzqyehv4eb_sk_-SF0Cy2yF21oW-SKUl4VYuVgc9m1uTCPzI3PHkyhmCNSu2O20YuEm7d9TRqNkmSwWOTkGVA4GsovB-TtVcSgMqXo3gOd22yVKb6h1PdlK8SngV44OaOiRP4U4paWNUlJL9Xj74p28SQUIadc7zCOKUvywBH9j7Yaub4X4Rko0Gp-AIngUp5czs63Z0YGYNvuRWwWnCZAZqhPHepQRGWZWLL0yVcs04TCW4jEd0ty3lFJb0sGHwQZDDYu-0Ixh4QLK-vkjiAHQyOzszyZQ_T3RsbjPyrnOM&pub=4a1b367933fd867b19b072952f68dceb&camk=ethIe0s0hefVEJOYVnGhcw%3D%3D&xkcb=SoC56_M3xMBSWL2Tb50ZbzkdCdPP&xpse=SoA66_I3xMBSHXTbtx0IbzkdCdPP&xfps=6e954f0d-cd46-4226-9181-741b6f9ea986&vjs=3"


class TrackerTests(TestCase):

    def test_validate_link(self):
        self.assertFalse(views.validate_link(none))
        self.assertFalse(views.validate_link(google))
        self.assertTrue(views.validate_link(linkedin))
        self.assertTrue(views.validate_link(ziprecruiter))
        self.assertTrue(views.validate_link(indeed))
        self.assertTrue(views.validate_link(glassdoor))
        self.assertTrue(views.validate_link(job1))

    def test_scrape_ziprecruiter(self):
        self.assertEqual(
            scraper.read_url(job2), "Full Stack Web Developer - In Person - Fairfield, NJ - Fairfield, NJ 07004 - Indeed.com"
        )

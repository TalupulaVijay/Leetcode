class Solution(object):
    def numUniqueEmails(self, emails):
        unique_emails = set()

        for email in emails:
            local, domain = email.split('@')
            local = local.split('+')[0].replace('.', '')
            normalized_email = local + '@' + domain
            unique_emails.add(normalized_email)

        return len(unique_emails)
        
        
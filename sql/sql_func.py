import sqlite3

# Insert functions
def insertCNAMEpacketsEntry(domainName, sourceAddress, CNAMEAlias, hasAType):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM CNAMEpackets WHERE domainName = ? AND sourceAddress = ? AND CNAMEAlias = ?", (domainName, sourceAddress, CNAMEAlias))
    result = cur.fetchone()
    
    # Check if a result of the same values already exists. If new result is same except for Atype, just update old value
    if (result):
        if (result[3] == 0 and hasAType == 1):
            cur.execute("UPDATE CNAMEpackets set hasAType = 1 WHERE domainName = ? AND sourceAddress = ? AND CNAMEAlias = ?", (domainName, sourceAddress, CNAMEAlias))
            conn.commit()
        conn.close()
        return

    # Insert into the database
    cur.execute("INSERT INTO CNAMEpackets VALUES (?, ?, ?, ?)", (domainName, sourceAddress, CNAMEAlias, hasAType))
    conn.commit()
    conn.close()
    return

def insertIpEntry(domainName, ip):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO ip VALUES (?, ?)", (domainName, ip))
    
    conn.commit()
    conn.close()
    return

def insertCookieEntry(domainName, src_ip, domain_setting, httponly, secure):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO cookie VALUES (?, ?, ?, ?, ?)", (domainName, src_ip, domain_setting, httponly, secure))
    
    conn.commit()
    conn.close()
    return

# Fetch functions

def fetchDomainFromAlias(CNAMEAlias):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute("SELECT domainName FROM CNAMEpackets WHERE CNAMEAlias = ?", (CNAMEAlias,))
    result = cur.fetchall()

    conn.commit()
    conn.close()
    return result

def fetchIpFromDomain(domainName):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute("SELECT ip FROM ip WHERE domainName = ?", (domainName,))
    result = cur.fetchall()
    return result

def fetchATypeRecordsFromDomain(domainName):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute("SELECT hasAType FROM CNAMEpackets WHERE domainName = ?", (domainName,))
    result = cur.fetchall()

    return result

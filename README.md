# system-design-server

## References

### Projects
#### 2 Phase Commit
- Participants
    - Client
    - Transcation Coordinator
    - Node 1 (with a value)
    - Node 2 (with a value)
- Supported Transaction
    - Transfer value from Node 1 to Node 2
- Phases
    - Voting phase : transaction coordinator will ask all nodes to respond
    - Decision phase : transaction will always be processed if both nodes voted yes
- Note
    - Messages have time-out
    - Each transcation has a unique ID
    - Locks need to be held on the node
    - Node will make sure the transcation will be commited before responding yes
    - WAL(write-ahead logs) is one way to resume from crashes


### Python
- [IMPORTERROR: ATTEMPTED RELATIVE IMPORT WITH NO KNOWN PARENT PACKAGE](https://iq-inc.com/importerror-attempted-relative-import/)
- [Running unittest with typical test directory structure](https://stackoverflow.com/questions/1896918/running-unittest-with-typical-test-directory-structure)
- [Python type declaration -- forward references](https://peps.python.org/pep-0484/#forward-references)

## Python test
Run the following command at the project root to run unit tests
```
python3 -m unittest tests.<file_name_without_extension>
```

describe('My First Test', function() {
  it('Visits the Web', function() {
    cy.visit('http://test.llau.systems')
    cy.contains('.navbar-burger').click()
  })
})
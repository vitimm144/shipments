describe('Shipment Test page', function() {
  beforeEach(() => {
    cy.visit('http://localhost:8080')
  })
  it('test the title', () => {
    // https://on.cypress.io/title
    cy.title().should('include', 'Shipment')
  })
  it('test add button', () => {
    cy.get("#modal-shipment").should('not.be.visible')
    cy.get('#add-button')
    .should('have.text', 'Add')
    .click()
    cy.get("#modal-shipment").should('be.visible')
  })
  it('test modal elements', () => {
    cy.get('#add-button').click()
    cy.get("#modal-shipment").contains('Shipment')
    cy.get("#modal-shipment").contains('Shipment Add')
    cy.get("#modal-shipment").contains('Sender Name:')
    cy.get("#modal-shipment").contains('Sender Address:')
    cy.get("#modal-shipment").contains('Recipient Name:')
    cy.get("#modal-shipment").contains('Recipient Address:')
    cy.get("#modal-shipment").contains('Postal Code:')
    cy.get("#modal-shipment").contains('Shipment Code:')
    cy.get('#sender-name')
      .should('have.attr', 'type', 'text')
    cy.get('#recipient-name')
      .should('have.attr', 'type', 'text')
    cy.get('#postal-code')
      .should('have.attr', 'type', 'text')
    cy.get('#shipment-code')
      .should('have.attr', 'type', 'text')
  })
  it('test table', () => {
    cy.get('.table')
    .contains('Id')
    cy.get('.table')
    .contains('Expedition')
    
    cy.get('.table')
    .contains('Sender Name')
    cy.get('.table')
    .contains('Sender Address')
    cy.get('.table')
    .contains('Recipient Name')
    cy.get('.table')
    .contains('Recipient Address')
    cy.get('.table')
    .contains('Postal Code')
    cy.get('.table')
    .contains('Shipment Code')
    cy.get('.table')
    .contains('Options')
  })

  
})
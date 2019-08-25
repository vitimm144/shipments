<template>
  <div id="app">
  
    <h1 class="">Shipments</h1> <b-button block variant="success" v-b-modal.modal-shipment>Add</b-button>
    <div>
        
    <b-modal ref="modal-shipment" id="modal-shipment" title="Shipment Add">
      <b-card bg-variant="light">
      <b-form-group
        label-cols-lg="3"
        label="Shipment"
        label-size="lg"
        label-class="font-weight-bold pt-0"
        class="mb-0"
      >
        <b-form-group
          label-cols-sm="3"
          label="Sender Name:"
          label-align-sm="right"
          label-for="sender-name"
        >
        <b-form-input id="sender-name" v-model="shipment.sender_name"></b-form-input>
        </b-form-group>

        <b-form-group
          label-cols-sm="3"
          label="Sender Address:"
          label-align-sm="right"
          label-for="sender-address"
        >
          <b-form-input id="sender-address" v-model="shipment.sender_address"></b-form-input>
        </b-form-group>

        <b-form-group
          label-cols-sm="3"
          label="Recipient Name:"
          label-align-sm="right"
          label-for="recipient-name"
        >
          <b-form-input id="recipient-name" v-model="shipment.recipient_name"></b-form-input>
        </b-form-group>
        <b-form-group
          label-cols-sm="3"
          label="Recipient Address:"
          label-align-sm="right"
          label-for="recipient-address"
        >
          <b-form-input id="recipient-address" v-model="shipment.recipient_address"></b-form-input>
        </b-form-group>

        <b-form-group
          label-cols-sm="3"
          label="Postal Code:"
          label-align-sm="right"
          label-for="postal-code"
        >
          <b-form-input id="postal-code" v-model="shipment.postal_code"></b-form-input>
        </b-form-group>
        <b-form-group
          label-cols-sm="3"
          label="Shipment Code:"
          label-align-sm="right"
          label-for="shipment-code"
        >
          <b-form-input id="shipment-code" v-model="shipment.shipment_code"></b-form-input>
        </b-form-group>
        
      </b-form-group>
      </b-card>
      <template slot="modal-footer">
        <b-button @click="saveShipment()">Send</b-button>

      </template>
      </b-modal>
    </div>

    <div>
       <b-table striped hover :items="items" :fields="fields">
         <template slot="[options]" slot-scope="row">
          <b-button variant="info" type="button" v-on:click="editShipment(row.item)"> Edit </b-button>
          <b-button variant="danger" type="button" v-on:click="deleteShipment(row.item)"> Remove </b-button>
          </template>
       </b-table>
    </div>  
    
    
  </div>
</template>

<script>
export default {
  name: 'app',
  data () {
    return {
      shipment: {
        "id":"",
        "sender_name":"",
        "recipient_name":"",
        "recipient_address":"",
        "postal_code":"",
        "shipment_code":""
      },
      text:'',
      endpoint:'http://localhost:8000/api/shipments/',
      list:[{"text":"blabasadas", "name":"Victor"}],
      msg: 'Welcome to Your Vue.js App',
      fields: [
        "id",
        "expedition",
        "sender_name",
        "sender_address",
        "recipient_name",
        "recipient_address",
        "postal_code",
        "shipment_code",
        "options" 
      ],
      items: [],
      config: {
          headers: {
            'Content-Type': 'application/json'
          }
        }



    }
  },
  methods:{
    addTodo(){
      this.list.push({text: this.text})
      this.text = ''
    },
    removeTodo(index){
      this.list.slice(index, 1)
    },
    saveShipment(){
      var method = 'post'
      var url = this.endpoint
      if (this.shipment.id){
        method = 'patch'
        url += this.shipment.id + '/'
      }
      this.$http[method](url, this.shipment, this.config).then(
        response => {
          console.log(response)

          this.updateGrid()
          this.$refs['modal-shipment'].hide()
        },
        response => {
          console.log(response)
        }
        
      )
    },
    editShipment(item){
      console.log(item)
      this.shipment = item
      this.$refs['modal-shipment'].show()
    },
    updateGrid(){
      this.$http.get(this.endpoint, this.config).then(
        response => {
          console.log(response)
          this.items = response.data.results
        },
        response => {
          console.log(response)
        }
      )
    },
    deleteShipment(item){
      var url = this.endpoint + item.id + '/'
      this.$http.delete(url, this.config).then(
        response => {
          console.log(response)
          this.updateGrid()
        }
      )
    }
    
  },
  beforeMount(){
    this.updateGrid()
  }
}
</script>